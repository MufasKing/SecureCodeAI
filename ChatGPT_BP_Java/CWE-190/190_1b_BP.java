import java.math.BigInteger;
import java.util.Scanner;

public class SecureOffsetAdder {

    // Define a constant offset of 1000
    private static final int OFFSET = 1000;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a valid integer:");

        // Secure handling for reading and validating input
        String input = scanner.nextLine().trim();
        
        // Input validation
        if (!isValidInteger(input)) {
            System.out.println("Error: Invalid input. Please enter a valid integer.");
            return;
        }
        
        // Convert input to BigInteger to prevent overflow/underflow
        BigInteger userInput;
        try {
            userInput = new BigInteger(input);
        } catch (NumberFormatException e) {
            System.out.println("Error: Input is not a valid integer.");
            return;
        }

        // Adding the offset in a secure manner
        BigInteger offset = BigInteger.valueOf(OFFSET);
        BigInteger result = userInput.add(offset);

        // Check for overflow
        if (result.compareTo(BigInteger.valueOf(Integer.MAX_VALUE)) > 0 ||
            result.compareTo(BigInteger.valueOf(Integer.MIN_VALUE)) < 0) {
            System.out.println("Error: The result is out of the valid integer range.");
        } else {
            System.out.println("Result after adding offset: " + result.intValue());
        }

        // Close the scanner resource securely
        scanner.close();
    }

    // Method to check if a string is a valid integer (with security in mind)
    private static boolean isValidInteger(String input) {
        if (input == null || input.isEmpty()) {
            return false;
        }

        // Regex to check for valid integers, including negative numbers
        String regex = "-?\\d+";
        return input.matches(regex);
    }
}
