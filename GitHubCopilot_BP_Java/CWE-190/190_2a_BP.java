import java.math.BigDecimal;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class 190_2a_BP {
    private static final Logger logger = Logger.getLogger(SecureApp.class.getName());

    public static void main(String[] args) {
        // Set up logging
        logger.setLevel(Level.ALL);

        Scanner scanner = new Scanner(System.in);
        BigDecimal number = null;

        try {
            // Input validation
            System.out.print("Enter a decimal number: ");
            String input = scanner.nextLine();
            if (!input.matches("\\d+(\\.\\d+)?")) {
                throw new IllegalArgumentException("Invalid input. Please enter a valid decimal number.");
            }

            // Use BigDecimal for precise decimal arithmetic
            number = new BigDecimal(input);
            logger.info("User entered a valid decimal number: " + number);

            // Perform some operations with BigDecimal
            BigDecimal result = number.multiply(new BigDecimal("2"));
            System.out.println("Result after multiplication by 2: " + result);

        } catch (IllegalArgumentException e) {
            logger.severe("Input validation error: " + e.getMessage());
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            logger.severe("An unexpected error occurred: " + e.getMessage());
            System.out.println("An unexpected error occurred. Please try again.");
        } finally {
            scanner.close();
            logger.info("Application finished execution.");
        }
    }
}