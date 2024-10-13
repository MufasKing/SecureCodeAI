package GitHubCopilot_BP_Java.CWE-522;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.util.Base64;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

public class Main {
    public static void main(String[] args) {
        RegistrationForm form = new RegistrationForm();
        form.registerUser("username", "password");
    }
}

class User {
    private String username;
    private String hashedPassword;
    private String salt;

    public User(String username, String hashedPassword, String salt) {
        this.username = username;
        this.hashedPassword = hashedPassword;
        this.salt = salt;
    }

    // Getters and setters
}

class PasswordUtils {
    private static final Logger logger = Logger.getLogger(PasswordUtils.class.getName());
    private static final int SALT_LENGTH = 16;
    private static final int ITERATIONS = 65536;
    private static final int KEY_LENGTH = 256;

    public static String generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[SALT_LENGTH];
        random.nextBytes(salt);
        return Base64.getEncoder().encodeToString(salt);
    }

    public static String hashPassword(String password, String salt) {
        try {
            PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt.getBytes(), ITERATIONS, KEY_LENGTH);
            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            byte[] hash = factory.generateSecret(spec).getEncoded();
            return Base64.getEncoder().encodeToString(hash);
        } catch (NoSuchAlgorithmException | InvalidKeySpecException e) {
            logger.log(Level.SEVERE, "Error hashing password", e);
            throw new RuntimeException("Error hashing password", e);
        }
    }

    public static boolean validatePassword(String originalPassword, String storedPassword, String salt) {
        String hashedPassword = hashPassword(originalPassword, salt);
        return hashedPassword.equals(storedPassword);
    }
}

class RegistrationForm {
    private static final Logger logger = Logger.getLogger(RegistrationForm.class.getName());

    public void registerUser(String username, String password) {
        if (!validateInput(username, password)) {
            logger.log(Level.WARNING, "Invalid input");
            return;
        }

        String salt = PasswordUtils.generateSalt();
        String hashedPassword = PasswordUtils.hashPassword(password, salt);

        User user = new User(username, hashedPassword, salt);
        storeUser(user);
        logger.log(Level.INFO, "User registered successfully");
    }

    private boolean validateInput(String username, String password) {
        if (username == null || username.isEmpty() || password == null || password.isEmpty()) {
            return false;
        }
        // Additional validation rules can be added here
        return true;
    }

    private void storeUser(User user) {
        // Securely store the user details (e.g., in a database)
        // This is a placeholder for actual storage logic
        logger.log(Level.INFO, "Storing user: " + user.getUsername());
    }
}