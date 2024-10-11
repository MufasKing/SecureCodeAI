import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.security.*;
import java.sql.*;
import java.util.Base64;
import java.util.regex.*;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

public class LoginServlet extends HttpServlet {

    // Database connection setup (Replace with your DB details)
    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASS = "yourpassword";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("logout".equals(action)) {
            request.getSession().invalidate();
            response.sendRedirect("index.jsp");
        } else {
            PrintWriter out = response.getWriter();
            out.println("<html><body>");
            out.println("<h2>Welcome to the Login Page</h2>");
            out.println("<form action='LoginServlet' method='POST'>");
            out.println("Username: <input type='text' name='username' required><br>");
            out.println("Password: <input type='password' name='password' required><br>");
            out.println("<input type='hidden' name='csrfToken' value='" + generateCSRFToken(request) + "'>");
            out.println("<input type='submit' value='Login'>");
            out.println("</form>");
            out.println("<a href='index.jsp'>Go to Index Page</a>");
            out.println("</body></html>");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String csrfToken = request.getParameter("csrfToken");
        if (!validateCSRFToken(request, csrfToken)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "CSRF token validation failed.");
            return;
        }

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (validateInput(username, password)) {
            try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS)) {
                String query = "SELECT password_hash FROM users WHERE username = ?";
                try (PreparedStatement stmt = conn.prepareStatement(query)) {
                    stmt.setString(1, username);
                    ResultSet rs = stmt.executeQuery();
                    if (rs.next()) {
                        String storedHash = rs.getString("password_hash");
                        if (verifyPassword(password, storedHash)) {
                            HttpSession session = request.getSession();
                            session.setAttribute("username", username);
                            response.sendRedirect("secret.jsp");
                        } else {
                            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid username or password.");
                        }
                    } else {
                        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid username or password.");
                    }
                }
            } catch (SQLException e) {
                log("Database error: " + e.getMessage());
                response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "An error occurred while accessing the database.");
            }
        } else {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input.");
        }
    }

    private boolean validateInput(String username, String password) {
        // Check password complexity
        String passwordRegex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[A-Za-z\\d]{8,}$"; // At least 8 characters, 1 uppercase, 1 number
        return username != null && password != null && password.matches(passwordRegex);
    }

    private String hashPassword(String password) throws Exception {
        byte[] salt = SecureRandom.getInstance("SHA1PRNG").generateSeed(16);
        PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
        byte[] hash = factory.generateSecret(spec).getEncoded();
        return Base64.getEncoder().encodeToString(salt) + ":" + Base64.getEncoder().encodeToString(hash);
    }

    private boolean verifyPassword(String password, String storedHash) throws Exception {
        String[] parts = storedHash.split(":");
        byte[] salt = Base64.getDecoder().decode(parts[0]);
        PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
        byte[] hash = factory.generateSecret(spec).getEncoded();
        return storedHash.equals(Base64.getEncoder().encodeToString(salt) + ":" + Base64.getEncoder().encodeToString(hash));
    }

    private String generateCSRFToken(HttpServletRequest request) {
        HttpSession session = request.getSession();
        String token = (String) session.getAttribute("csrfToken");
        if (token == null) {
            token = Base64.getEncoder().encodeToString(SecureRandom.getInstance("SHA1PRNG").generateSeed(16));
            session.setAttribute("csrfToken", token);
        }
        return token;
    }

    private boolean validateCSRFToken(HttpServletRequest request, String csrfToken) {
        HttpSession session = request.getSession();
        String storedToken = (String) session.getAttribute("csrfToken");
        return storedToken != null && storedToken.equals(csrfToken);
    }

    @Override
    public void init() throws ServletException {
        super.init();
        // Set security headers
        getServletContext().setInitParameter("Header-X-Content-Type-Options", "nosniff");
        getServletContext().setInitParameter("Header-X-XSS-Protection", "1; mode=block");
        getServletContext().setInitParameter("Header-X-Frame-Options", "DENY");
        getServletContext().setInitParameter("Header-Strict-Transport-Security", "max-age=31536000; includeSubDomains");
    }
}
