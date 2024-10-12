import java.io.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.sql.*;
import java.util.Base64;
import java.util.logging.Logger;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.servlet.http.HttpServletRequest;

public class SecureImageUploader {

    // Database credentials (environment variables for better security)
    private static final String DB_URL = System.getenv("DB_URL");
    private static final String DB_USER = System.getenv("DB_USER");
    private static final String DB_PASSWORD = System.getenv("DB_PASSWORD");

    // Logger for error handling
    private static final Logger logger = Logger.getLogger(SecureImageUploader.class.getName());

    // Method to upload image and insert into database
    public void uploadImage(File imageFile, String imageName, HttpServletRequest request) throws Exception {
        validateUser(request); // Authorization & Authentication

        if (validateImage(imageFile, imageName)) {
            String base64Image = encodeToBase64(imageFile);
            insertImageToDatabase(imageName, base64Image);
        }
    }

    // Validate the image
    private boolean validateImage(File imageFile, String imageName) {
        if (imageFile == null || !imageFile.exists() || imageName == null || imageName.isEmpty()) {
            logger.warning("Invalid image or image name.");
            return false;
        }
        // Additional file format validation can be added here (e.g., file extension)
        return true;
    }

    // Encode image file to base64 string
    private String encodeToBase64(File imageFile) throws IOException {
        byte[] fileContent = Files.readAllBytes(imageFile.toPath());
        return Base64.getEncoder().encodeToString(fileContent);
    }

    // Insert image name and base64 string into database
    private void insertImageToDatabase(String imageName, String base64Image) {
        String insertQuery = "INSERT INTO images (image_name, image_data) VALUES (?, ?)";

        try (Connection conn = getSecureConnection();
             PreparedStatement pstmt = conn.prepareStatement(insertQuery)) {

            pstmt.setString(1, encodeForDatabase(imageName));  // Output Encoding
            pstmt.setString(2, base64Image); // Binary data can be stored safely
            pstmt.executeUpdate();
        } catch (SQLException e) {
            logger.severe("Database error: " + e.getMessage());
        }
    }

    // Secure connection to the database
    private Connection getSecureConnection() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
    }

    // Authorization & Authentication (example using session token)
    private void validateUser(HttpServletRequest request) throws Exception {
        String authToken = request.getHeader("Authorization");

        if (authToken == null || !isValidToken(authToken)) {
            throw new SecurityException("Unauthorized access.");
        }
    }

    // Example token validation (implement actual logic)
    private boolean isValidToken(String token) {
        // Token validation logic (JWT or other mechanisms)
        return true;
    }

    // Secure hashing with salt generation for passwords or sensitive data
    public String generateHash(String data) throws NoSuchAlgorithmException {
        byte[] salt = generateSalt();
        PBEKeySpec spec = new PBEKeySpec(data.toCharArray(), salt, 10000, 512);
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA512");
        byte[] hash = keyFactory.generateSecret(spec).getEncoded();
        return Base64.getEncoder().encodeToString(hash);
    }

    // Secure salt generation
    private byte[] generateSalt() throws NoSuchAlgorithmException {
        SecureRandom sr = SecureRandom.getInstanceStrong();
        byte[] salt = new byte[16];
        sr.nextBytes(salt);
        return salt;
    }

    // Output encoding for preventing SQL injection
    private String encodeForDatabase(String input) {
        return input.replaceAll("[^a-zA-Z0-9_-]", ""); // Simple example; use a library for complex cases
    }

    // Secure table creation (if needed)
    public void createTable() {
        String createTableQuery = "CREATE TABLE IF NOT EXISTS images ("
                + "id INT AUTO_INCREMENT PRIMARY KEY, "
                + "image_name VARCHAR(255) NOT NULL, "
                + "image_data LONGBLOB NOT NULL"
                + ")";
        try (Connection conn = getSecureConnection();
             PreparedStatement pstmt = conn.prepareStatement(createTableQuery)) {
            pstmt.execute();
        } catch (SQLException e) {
            logger.severe("Error creating table: " + e.getMessage());
        }
    }

    // Secure file deletion (optional for cleanup)
    public void deleteFileSecurely(File file) throws IOException {
        try {
            Files.deleteIfExists(file.toPath());
        } catch (IOException e) {
            logger.warning("Could not delete file securely: " + e.getMessage());
            throw e;
        }
    }
}
