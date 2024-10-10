import java.util.Scanner;

public class SecureAddition {

    public static void main(String[] args) {
        // Call function to handle the logic
        int result = performAddition();
        // Explicit exit with return code 0 (successful)
        System.exit(result);
    }

    /**
     * This method handles reading input, validating it, performing the addition, and printing the result.
     * @return 0 if the operation was successful, otherwise returns non-zero code for failure
     */
    private static int performAddition() {
        Scanner scanner = null;
        try {
            // Initialize Scanner for secure input reading
            scanner = new Scanner(System.in);
            System.out.println("Enter a number:");

            // Secure input conversion with validation
            String input = scanner.nextLine();
            int number = validateAndConvertInput(input);

            // Perform the addition operation
            int result = addThousand(number);

            // Print the result
            System.out.println("The result is: " + result);

            // Return success code
            return 0;
        } catch (NumberFormatException e) {
            // Handle number format exception (invalid input)
            System.err.println("Error: Invalid input. Please enter a valid integer.");
            return 1; // Return non-zero code to indicate error
        } catch (Exception e) {
            // Handle any other unexpected exceptions
            System.err.println("An unexpected error occurred: " + e.getMessage());
            return 2; // Return a different non-zero code to indicate other errors
        } finally {
            if (scanner != null) {
                scanner.close(); // Close scanner resource
            }
        }
    }

    /**
     * Validates the input and converts it into an integer.
     * @param input - the input string from the user
     * @return the parsed integer value
     * @throws NumberFormatException if the input is not a valid integer
     */
    private static int validateAndConvertInput(String input) throws NumberFormatException {
        // Ensure input is not null or empty
        if (input == null || input.trim().isEmpty()) {
            throw new NumberFormatException("Input cannot be null or empty.");
        }

        // Parse input to integer with NumberFormatException handling
        return Integer.parseInt(input.trim());
    }

    /**
     * Adds 1000 to the provided number.
     * @param number the original number input
     * @return the result after adding 1000
     */
    private static int addThousand(final int number) {
        return number + 1000;
    }
}
