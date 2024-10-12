import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.regex.Pattern;
import javax.servlet.http.HttpServletRequest;

public class UserRegistration {

    // Database configuration
    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASSWORD = "yourpassword";
    
    // Rate limiting configuration
    private static final int MAX_ATTEMPTS = 5;
    private static int loginAttempts = 0;

    // Password policy regex
    private static final Pattern PASSWORD_POLICY = Pattern.compile("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$");

    public static void main(String[] args) {
        // Simulate user input (in a real application, this would come from a web form)
        String username = "exampleUser"; // Replace with user input
        String password = "SecureP@ssw0rd"; // Replace with user input
        
        // Validate input
        if (validateInput(username, password)) {
            // Generate salt and hash password
            try {
                String salt = generateSalt();
                String hashedPassword = hashPassword(password, salt);
                
                // Insert into database
                insertUserIntoDatabase(username, hashedPassword, salt);
                System.out.println("User registered successfully!");
            } catch (Exception e) {
                System.err.println("Error during registration: " + e.getMessage());
            }
        } else {
            System.err.println("Password does not meet policy requirements.");
        }
    }

    private static boolean validateInput(String username, String password) {
        return username != null && !username.trim().isEmpty() && PASSWORD_POLICY.matcher(password).matches();
    }

    private static String generateSalt() {
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);
        return bytesToHex(salt);
    }

    private static String hashPassword(String password, String salt) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(hexToBytes(salt));
            md.update(password.getBytes());
            return bytesToHex(md.digest());
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }

    private static void insertUserIntoDatabase(String username, String hashedPassword, String salt) throws SQLException {
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String sql = "INSERT INTO users (username, password, salt) VALUES (?, ?, ?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
                pstmt.setString(1, username);
                pstmt.setString(2, hashedPassword);
                pstmt.setString(3, salt);
                pstmt.executeUpdate();
            }
        }
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    private static byte[] hexToBytes(String hex) {
        int len = hex.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(hex.charAt(i), 16) << 4)
                                 + Character.digit(hex.charAt(i + 1), 16));
        }
        return data;
    }

    // Dummy CSRF protection
    private static boolean isValidCsrfToken(HttpServletRequest request) {
        // This method should validate the CSRF token sent with the request
        return true; // Implement your logic here
    }

    // Rate limiting enforcement
    private static boolean isRateLimited() {
        if (loginAttempts >= MAX_ATTEMPTS) {
            System.err.println("Too many login attempts. Please try again later.");
            return true;
        }
        return false;
    }

    // Logging (placeholder for actual logging implementation)
    private static void log(String message) {
        System.out.println("LOG: " + message);
    }
}
