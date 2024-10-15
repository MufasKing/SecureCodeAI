package GitHubCopilot_BP_Java.CWE_522;

import java.sql.*;
import java.security.SecureRandom;
import java.util.regex.Pattern;
import org.mindrot.jbcrypt.BCrypt;

public class Registration {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASSWORD = "yourpassword";

    public static void main(String[] args) {
        // Example usage
        String result = registerUser("newuser", "password123", "John", "Doe", "john.doe@example.com", "csrfToken");
        System.out.println(result);
    }

    public static String registerUser(String username, String password, String firstName, String lastName, String email, String csrfToken) {
        if (!validateInput(username, firstName, lastName, email) || !validateCsrfToken(csrfToken)) {
            return "Invalid input or CSRF token.";
        }

        String hashedPassword = hashPassword(password);

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            if (isUsernameExists(conn, username)) {
                return "Username already exists.";
            }

            insertUser(conn, username, hashedPassword, firstName, lastName, email);
            return "Registration succeeded.";
        } catch (SQLException e) {
            e.printStackTrace();
            return "Database error.";
        }
    }

    private static boolean validateInput(String username, String firstName, String lastName, String email) {
        String regex = "^[a-zA-Z0-9._-]{3,}$";
        Pattern pattern = Pattern.compile(regex);
        return pattern.matcher(username).matches() && pattern.matcher(firstName).matches() && pattern.matcher(lastName).matches() && email.contains("@");
    }

    private static boolean validateCsrfToken(String csrfToken) {
        // Implement CSRF token validation logic here
        return csrfToken != null && !csrfToken.isEmpty();
    }

    private static String hashPassword(String password) {
        return BCrypt.hashpw(password, BCrypt.gensalt(12, new SecureRandom()));
    }

    private static boolean isUsernameExists(Connection conn, String username) throws SQLException {
        String query = "SELECT COUNT(*) FROM users WHERE username = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, username);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1) > 0;
                }
            }
        }
        return false;
    }

    private static void insertUser(Connection conn, String username, String hashedPassword, String firstName, String lastName, String email) throws SQLException {
        String query = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, username);
            stmt.setString(2, hashedPassword);
            stmt.setString(3, firstName);
            stmt.setString(4, lastName);
            stmt.setString(5, email);
            stmt.executeUpdate();
        }
    }
}