import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegistrationForm {

    private static final int SALT_LENGTH = 16; // Salt length in bytes
    private static final String PASSWORD_REGEX = "^(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$"; // Password must be at least 8 characters with letters and numbers
    private static final String LOG_FILE = "registration_log.txt"; // Log file path

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        if (!isValidPassword(password)) {
            System.out.println("Password does not meet policy requirements.");
            logError("Invalid password for user: " + username);
            return;
        }

        try {
            // Generate salt and hash the password
            byte[] salt = generateSalt();
            String hashedPassword = hashPassword(password, salt);

            // Securely store the username and hashed password
            storeUserData(username, hashedPassword, salt);
            System.out.println("Registration successful!");

        } catch (Exception e) {
            System.out.println("An error occurred during registration: " + e.getMessage());
            logError("Registration error for user: " + username + " - " + e.getMessage());
        }

        scanner.close();
    }

    private static boolean isValidPassword(String password) {
        Pattern pattern = Pattern.compile(PASSWORD_REGEX);
        Matcher matcher = pattern.matcher(password);
        return matcher.matches();
    }

    private static byte[] generateSalt() {
        SecureRandom sr = new SecureRandom();
        byte[] salt = new byte[SALT_LENGTH];
        sr.nextBytes(salt);
        return salt;
    }

    private static String hashPassword(String password, byte[] salt) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(salt);
        byte[] hashedPassword = md.digest(password.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(hashedPassword);
    }

    private static void storeUserData(String username, String hashedPassword, byte[] salt) {
        // In a real application, you'd store this data in a secure database
        System.out.println("Storing user data...");
        System.out.println("Username: " + username);
        System.out.println("Hashed Password: " + hashedPassword);
        System.out.println("Salt: " + Base64.getEncoder().encodeToString(salt));
        logSuccess("User registered successfully: " + username);
    }

    private static void logError(String message) {
        // Log errors (in a real application, write to a logging framework or file)
        System.err.println("ERROR: " + message);
    }

    private static void logSuccess(String message) {
        // Log success messages
        System.out.println("SUCCESS: " + message);
    }
}

