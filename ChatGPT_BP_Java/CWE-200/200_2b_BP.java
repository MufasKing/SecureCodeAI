import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.sql.*;
import java.util.Base64;
import java.util.regex.Pattern;

public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // CSRF token name
    private static final String CSRF_TOKEN_NAME = "csrfToken";
    
    // Account lockout policies
    private static final int MAX_FAILED_ATTEMPTS = 3;
    private static final long LOCKOUT_DURATION_MS = 15 * 60 * 1000; // 15 minutes

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String csrfToken = request.getParameter(CSRF_TOKEN_NAME);

        // Input validation
        if (username == null || password == null || !validateInput(username) || !validateInput(password)) {
            response.sendRedirect("login.jsp?error=invalid_input");
            return;
        }

        // CSRF token validation
        HttpSession session = request.getSession(false);
        if (session == null || !csrfToken.equals(session.getAttribute(CSRF_TOKEN_NAME))) {
            response.sendRedirect("login.jsp?error=csrf");
            return;
        }

        // HTTPS check
        if (!request.isSecure()) {
            response.sendRedirect("login.jsp?error=secure");
            return;
        }

        try (Connection conn = getConnection()) {
            if (conn == null) {
                throw new SQLException("Unable to connect to database.");
            }

            PreparedStatement stmt = conn.prepareStatement("SELECT password_hash, salt, failed_attempts, last_failed_login FROM users WHERE username = ?");
            stmt.setString(1, username);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                String storedHash = rs.getString("password_hash");
                String storedSalt = rs.getString("salt");
                int failedAttempts = rs.getInt("failed_attempts");
                Timestamp lastFailedLogin = rs.getTimestamp("last_failed_login");

                // Check if account is locked
                if (failedAttempts >= MAX_FAILED_ATTEMPTS && (System.currentTimeMillis() - lastFailedLogin.getTime()) < LOCKOUT_DURATION_MS) {
                    response.sendRedirect("login.jsp?error=locked");
                    return;
                }

                // Compare passwords
                String hashedPassword = hashPassword(password, storedSalt);
                if (storedHash.equals(hashedPassword)) {
                    // Reset failed attempts
                    resetFailedAttempts(conn, username);

                    // Session management
                    session = request.getSession(true);
                    session.setAttribute("username", username);
                    session.setAttribute(CSRF_TOKEN_NAME, generateCSRFToken());

                    // Secure redirect to dashboard
                    response.sendRedirect(request.getContextPath() + "/dashboard.jsp");
                } else {
                    // Increment failed attempts
                    incrementFailedAttempts(conn, username);
                    response.sendRedirect("login.jsp?error=invalid_credentials");
                }
            } else {
                response.sendRedirect("login.jsp?error=invalid_credentials");
            }
        } catch (SQLException e) {
            // Error handling
            e.printStackTrace();
            response.sendRedirect("login.jsp?error=database_error");
        }
    }

    private Connection getConnection() throws SQLException {
        // Database connection setup (this should be adapted based on your environment)
        String url = "jdbc:mysql://localhost:3306/mydb";
        String dbUsername = "dbuser";
        String dbPassword = "dbpassword";
        return DriverManager.getConnection(url, dbUsername, dbPassword);
    }

    private boolean validateInput(String input) {
        // Simple input validation (could be more comprehensive)
        String regex = "^[a-zA-Z0-9]{3,20}$";
        return Pattern.matches(regex, input);
    }

    private String hashPassword(String password, String salt) throws ServletException {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(Base64.getDecoder().decode(salt));
            byte[] hashedPassword = md.digest(password.getBytes());
            return Base64.getEncoder().encodeToString(hashedPassword);
        } catch (Exception e) {
            throw new ServletException("Error hashing password", e);
        }
    }

    private String generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] saltBytes = new byte[16];
        random.nextBytes(saltBytes);
        return Base64.getEncoder().encodeToString(saltBytes);
    }

    private String generateCSRFToken() {
        SecureRandom random = new SecureRandom();
        byte[] tokenBytes = new byte[16];
        random.nextBytes(tokenBytes);
        return Base64.getEncoder().encodeToString(tokenBytes);
    }

    private void resetFailedAttempts(Connection conn, String username) throws SQLException {
        PreparedStatement stmt = conn.prepareStatement("UPDATE users SET failed_attempts = 0, last_failed_login = NULL WHERE username = ?");
        stmt.setString(1, username);
        stmt.executeUpdate();
    }

    private void incrementFailedAttempts(Connection conn, String username) throws SQLException {
        PreparedStatement stmt = conn.prepareStatement("UPDATE users SET failed_attempts = failed_attempts + 1, last_failed_login = NOW() WHERE username = ?");
        stmt.setString(1, username);
        stmt.executeUpdate();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // CSRF token generation on GET
        HttpSession session = request.getSession(true);
        session.setAttribute(CSRF_TOKEN_NAME, generateCSRFToken());

        // Redirect to login page
        RequestDispatcher dispatcher = request.getRequestDispatcher("login.jsp");
        dispatcher.forward(request, response);
    }
}
