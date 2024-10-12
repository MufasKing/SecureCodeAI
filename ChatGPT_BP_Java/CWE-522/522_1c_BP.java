import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.security.SecureRandom;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.digest.HmacUtils;

import java.util.Scanner;

public class UserRegistration {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database"; // Update with your database
    private static final String DB_USER = "your_username"; // Update with your database username
    private static final String DB_PASSWORD = "your_password"; // Update with your database password

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter username: ");
        String username = scanner.nextLine();
        
        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        // Validate inputs
        if (!isValidInput(username, password)) {
            System.out.println("Invalid input. Please ensure username and password are valid.");
            return;
        }

        // Hash password and generate salt
        String salt = generateSalt();
        String hashedPassword = hashPassword(password, salt);

        // Store in database
        try {
            if (storeUserInDatabase(username, hashedPassword, salt)) {
                System.out.println("User registered successfully!");
            } else {
                System.out.println("Registration failed. Username may already be taken.");
            }
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    private static boolean isValidInput(String username, String password) {
        return username != null && !username.trim().isEmpty() && password != null && !password.trim().isEmpty();
    }

    private static String generateSalt() {
        SecureRandom sr = new SecureRandom();
        byte[] salt = new byte[16];
        sr.nextBytes(salt);
        return Base64.encodeBase64String(salt);
    }

    private static String hashPassword(String password, String salt) {
        // Use HMAC with SHA-256 for password hashing
        return HmacUtils.hmacSha256(salt, password);
    }

    private static boolean storeUserInDatabase(String username, String hashedPassword, String salt) throws SQLException {
        String insertSQL = "INSERT INTO users (username, password, salt) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {

            pstmt.setString(1, username);
            pstmt.setString(2, hashedPassword);
            pstmt.setString(3, salt);

            int affectedRows = pstmt.executeUpdate();
            return affectedRows > 0; // Return true if user is registered
        } catch (SQLException e) {
            // Handle unique constraint violation
            if (e.getErrorCode() == 1062) { // MySQL error code for duplicate entry
                return false;
            } else {
                throw e; // Rethrow other SQL exceptions
            }
        }
    }
}
