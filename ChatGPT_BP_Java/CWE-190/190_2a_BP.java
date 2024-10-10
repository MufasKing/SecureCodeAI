// Importing necessary modules
import java.math.BigDecimal;  // For precise decimal calculations
import java.util.Scanner;     // For input handling
import java.util.logging.*;   // For logging purposes
import javax.crypto.*;        // For encryption (data protection)
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.security.Key;

public class SecureApp {
    // Logger instance for logging and auditing
    private static final Logger logger = Logger.getLogger(SecureApp.class.getName());

    // Secret key for encryption (this is just an example, use secure key storage in production)
    private static final String SECRET_KEY = "1234567890123456"; // 16-char secret key for AES

    public static void main(String[] args) {
        // Configure the logger
        configureLogger();

        Scanner scanner = new Scanner(System.in);
        try {
            // Input validation with error handling
            System.out.print("Enter a decimal number: ");
            String input = scanner.nextLine();
            
            // Validate if the input is a valid decimal
            if (!input.matches("\\d+(\\.\\d+)?")) {
                throw new IllegalArgumentException("Invalid decimal number format");
            }

            // Use BigDecimal for secure and precise decimal arithmetic
            BigDecimal decimalValue = new BigDecimal(input);
            logger.info("User entered a valid decimal value: " + decimalValue);

            // Example operation with BigDecimal
            BigDecimal result = decimalValue.multiply(new BigDecimal("2.5"));
            System.out.println("Result after multiplication: " + result);

            // Encrypting data (for data protection)
            String encryptedData = encrypt(decimalValue.toString());
            logger.info("Encrypted data: " + encryptedData);

            // Decrypt and display (for demonstration purposes)
            String decryptedData = decrypt(encryptedData);
            System.out.println("Decrypted value: " + decryptedData);

        } catch (IllegalArgumentException e) {
            logger.severe("Input validation failed: " + e.getMessage());
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            logger.severe("An unexpected error occurred: " + e.getMessage());
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    // Method to configure logger for auditing
    private static void configureLogger() {
        try {
            LogManager.getLogManager().readConfiguration(SecureApp.class.getResourceAsStream("/logging.properties"));
        } catch (Exception e) {
            System.err.println("Error setting up logger: " + e.getMessage());
        }
    }

    // Method to encrypt a string (for data protection)
    private static String encrypt(String data) throws Exception {
        Key aesKey = new SecretKeySpec(SECRET_KEY.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, aesKey);
        byte[] encrypted = cipher.doFinal(data.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }

    // Method to decrypt an encrypted string
    private static String decrypt(String encryptedData) throws Exception {
        Key aesKey = new SecretKeySpec(SECRET_KEY.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, aesKey);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(encryptedData));
        return new String(decrypted);
    }
}
