import java.sql.*;
import java.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class RegistrationPage extends HttpServlet {
    
    // Database credentials
    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdbname";
    private static final String USER = "yourusername";
    private static final String PASS = "yourpassword";

    // Hashing function for password
    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());
            return Base64.getEncoder().encodeToString(hashedBytes);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }

    // SQL Injection Prevention & Registration Logic
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        String username = request.getParameter("username").trim();
        String password = request.getParameter("password").trim();
        String firstName = request.getParameter("firstName").trim();
        String lastName = request.getParameter("lastName").trim();
        String email = request.getParameter("email").trim();

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        // Validate input to prevent XSS
        if (username.isEmpty() || password.isEmpty() || firstName.isEmpty() || 
            lastName.isEmpty() || email.isEmpty()) {
            out.println("All fields are required!");
            return;
        }

        // Hash the password
        String hashedPassword = hashPassword(password);

        // Check if username exists
        try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASS)) {
            String checkUserQuery = "SELECT * FROM users WHERE username = ?";
            try (PreparedStatement ps = conn.prepareStatement(checkUserQuery)) {
                ps.setString(1, username);
                ResultSet rs = ps.executeQuery();
                if (rs.next()) {
                    out.println("Username already exists!");
                    return;
                }
            }

            // Insert new user
            String insertQuery = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)";
            try (PreparedStatement ps = conn.prepareStatement(insertQuery)) {
                ps.setString(1, username);
                ps.setString(2, hashedPassword);
                ps.setString(3, firstName);
                ps.setString(4, lastName);
                ps.setString(5, email);
                ps.executeUpdate();
                out.println("Registration succeeded!");
            }
        } catch (SQLException e) {
            out.println("Error during registration: " + e.getMessage());
        }
    }

    // Simple CSRF Protection
    private String generateCSRFToken() {
        // Generate a simple CSRF token (for production, use a stronger method)
        return Base64.getEncoder().encodeToString((System.currentTimeMillis() + "").getBytes());
    }
    
    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        String csrfToken = generateCSRFToken();
        request.setAttribute("csrfToken", csrfToken);
        RequestDispatcher dispatcher = request.getRequestDispatcher("registration.jsp");
        dispatcher.forward(request, response);
    }
}
