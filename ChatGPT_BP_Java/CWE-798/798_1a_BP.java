import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

public class UserAuth {

    // A simple in-memory "database" for demonstration purposes
    private static final Map<String, String> userDatabase = new HashMap<>();

    static {
        // For demonstration, we pre-populate the database with a user
        String username = "admin";
        String password = "password123"; // This should be securely stored
        String hashedPassword = hashPassword(password);
        userDatabase.put(username, hashedPassword);
    }

    public static void main(String[] args) {
        String username = "admin"; // Assume this is obtained from the form
        String password = "password123"; // Assume this is obtained from the form

        boolean isAuthenticated = check_mod(username, password);
        System.out.println("Authentication successful: " + isAuthenticated);
    }

    public static boolean check_mod(String username, String password) {
        // Input Validation
        if (!isValidInput(username) || !isValidInput(password)) {
            return false;
        }

        // Retrieve the stored password hash
        String storedPasswordHash = userDatabase.get(username);
        if (storedPasswordHash == null) {
            return false; // User not found
        }

        // Secure constant-time comparison of the hashes
        return constantTimeCompare(storedPasswordHash, hashPassword(password));
    }

    private static boolean isValidInput(String input) {
        // Simple validation: Check if input is not null and not empty
        return input != null && !input.trim().isEmpty();
    }

    private static String hashPassword(String password) {
        try {
            // Generate a salt
            byte[] salt = createSalt();
            // Hash the password with the salt
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(salt);
            byte[] hashedBytes = md.digest(password.getBytes());

            // Store the salt and the hash together
            byte[] combined = new byte[salt.length + hashedBytes.length];
            System.arraycopy(salt, 0, combined, 0, salt.length);
            System.arraycopy(hashedBytes, 0, combined, salt.length, hashedBytes.length);
            return Base64.getEncoder().encodeToString(combined);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Hashing algorithm not found", e);
        }
    }

    private static byte[] createSalt() {
        SecureRandom sr = new SecureRandom();
        byte[] salt = new byte[16]; // 128-bit salt
        sr.nextBytes(salt);
        return salt;
    }

    private static boolean constantTimeCompare(String storedHash, String providedHash) {
        byte[] hash1 = Base64.getDecoder().decode(storedHash);
        byte[] hash2 = Base64.getDecoder().decode(providedHash);

        if (hash1.length != hash2.length) {
            return false;
        }

        int result = 0;
        for (int i = 0; i < hash1.length; i++) {
            result |= hash1[i] ^ hash2[i]; // XOR operation
        }

        return result == 0; // Returns true if both hashes are the same
    }
}
