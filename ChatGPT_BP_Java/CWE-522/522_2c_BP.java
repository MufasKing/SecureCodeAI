import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;

public class RegistrationForm {

    // Method to generate a secure random salt
    private static byte[] generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[16]; // 16 bytes = 128 bits
        random.nextBytes(salt);
        return salt;
    }

    // Method to hash the password with the salt
    private static String hashPassword(String password, byte[] salt) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(salt);
        byte[] hashedPassword = md.digest(password.getBytes());
        return bytesToHex(hashedPassword);
    }

    // Method to convert bytes to hexadecimal
    private static String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

    // Method to validate user input
    private static boolean validateInput(String username, String password) {
        return username != null && !username.trim().isEmpty() && 
               password != null && password.length() >= 8; // Minimum password length
    }

    // Main method to run the registration form
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Registration Form");
        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password (minimum 8 characters): ");
        String password = scanner.nextLine();

        // Validate user input
        if (!validateInput(username, password)) {
            System.err.println("Error: Invalid input. Ensure username is not empty and password is at least 8 characters long.");
            return;
        }

        try {
            // Generate salt and hash the password
            byte[] salt = generateSalt();
            String hashedPassword = hashPassword(password, salt);
            
            // Simulate database storage (replace this with actual database code)
            storeInDatabase(username, hashedPassword, salt);

            System.out.println("Registration successful!");

        } catch (NoSuchAlgorithmException e) {
            System.err.println("Error: Password hashing algorithm not found.");
            e.printStackTrace();
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }

    // Simulated database storage method
    private static void storeInDatabase(String username, String hashedPassword, byte[] salt) {
        // Convert salt to Base64 for storage
        String saltBase64 = Base64.getEncoder().encodeToString(salt);
        System.out.printf("Storing in database: \nUsername: %s\nHashed Password: %s\nSalt: %s%n", username, hashedPassword, saltBase64);
    }
}
