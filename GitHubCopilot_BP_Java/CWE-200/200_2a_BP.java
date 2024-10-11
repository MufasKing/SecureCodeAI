import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Database credentials with least privilege
    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydb";
    private static final String DB_USER = "limited_user";
    private static final String DB_PASSWORD = "password";

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Set Content Security Policy header
        response.setHeader("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self';");

        // Validate input
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        if (username == null || password == null || username.isEmpty() || password.isEmpty()) {
            response.sendRedirect("cant_login");
            return;
        }

        // Hash the password
        String hashedPassword = hashPassword(password);

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, username);
                stmt.setString(2, hashedPassword);
                try (ResultSet rs = stmt.executeQuery()) {
                    if (rs.next()) {
                        // User found, create session
                        HttpSession session = request.getSession();
                        session.setAttribute("user", username);
                        response.sendRedirect("success");
                    } else {
                        // User not found
                        response.sendRedirect("cant_login");
                    }
                }
            }
        } catch (SQLException e) {
            // Handle SQL error
            response.sendRedirect("internal_server_error");
        }
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : hashedBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}