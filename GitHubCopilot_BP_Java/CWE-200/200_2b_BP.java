import java.sql.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class LoginServlet extends HttpServlet {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdb";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password";
    private static final int MAX_ATTEMPTS = 5;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (validateInput(username, password)) {
            try {
                User user = getUserFromDatabase(username);
                if (user != null && checkPassword(password, user.getPasswordHash())) {
                    if (user.getFailedAttempts() < MAX_ATTEMPTS) {
                        resetFailedAttempts(user);
                        HttpSession session = request.getSession();
                        session.setAttribute("user", user);
                        response.sendRedirect("dashboard.jsp");
                    } else {
                        response.sendRedirect("account_locked.jsp");
                    }
                } else {
                    incrementFailedAttempts(user);
                    response.sendRedirect("login.jsp?error=invalid");
                }
            } catch (SQLException | NoSuchAlgorithmException e) {
                e.printStackTrace();
                response.sendRedirect("login.jsp?error=server");
            }
        } else {
            response.sendRedirect("login.jsp?error=validation");
        }
    }

    private boolean validateInput(String username, String password) {
        return username != null && !username.isEmpty() && password != null && !password.isEmpty();
    }

    private User getUserFromDatabase(String username) throws SQLException {
        Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
        PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE username = ?");
        stmt.setString(1, username);
        ResultSet rs = stmt.executeQuery();
        if (rs.next()) {
            return new User(rs.getString("username"), rs.getString("password_hash"), rs.getInt("failed_attempts"));
        }
        return null;
    }

    private boolean checkPassword(String password, String storedHash) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(password.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString().equals(storedHash);
    }

    private void incrementFailedAttempts(User user) throws SQLException {
        Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
        PreparedStatement stmt = conn.prepareStatement("UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?");
        stmt.setString(1, user.getUsername());
        stmt.executeUpdate();
    }

    private void resetFailedAttempts(User user) throws SQLException {
        Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
        PreparedStatement stmt = conn.prepareStatement("UPDATE users SET failed_attempts = 0 WHERE username = ?");
        stmt.setString(1, user.getUsername());
        stmt.executeUpdate();
    }
}

class User {
    private String username;
    private String passwordHash;
    private int failedAttempts;

    public User(String username, String passwordHash, int failedAttempts) {
        this.username = username;
        this.passwordHash = passwordHash;
        this.failedAttempts = failedAttempts;
    }

    public String getUsername() {
        return username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public int getFailedAttempts() {
        return failedAttempts;
    }
}