import java.util.Arrays;

public class SecureArrayAccess {

    public static void main(String[] args) {
        // Example array for demonstration
        int[] exampleArray = {10, 20, 30, 40, 50};

        // Ensure exactly one argument is provided
        if (args.length != 1) {
            System.out.println("Error: Please provide a single integer as a command line argument.");
            return;
        }

        try {
            // Secure type conversion from String to int with bounds checking
            int index = parseAndValidateInput(args[0], exampleArray.length);
            
            // Access the array and print the corresponding value
            if (index != -1) { // -1 indicates invalid input
                System.out.println("Element at index " + index + ": " + exampleArray[index]);
            } else {
                System.out.println("Invalid input: Index out of bounds.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Error: Input is not a valid integer.");
        } catch (Exception e) {
            System.out.println("Error: An unexpected error occurred.");
        }
    }

    /**
     * Securely parses the input string and validates it against array bounds.
     * 
     * @param input The command line input argument as a string
     * @param arrayLength The length of the array to check bounds against
     * @return A valid integer index or -1 if the input is out of bounds
     * @throws NumberFormatException if the input is not a valid integer
     */
    private static int parseAndValidateInput(String input, int arrayLength) throws NumberFormatException {
        // Convert the input to an integer securely
        int index = Integer.parseInt(input);

        // Check if the index is within the valid range of the array
        if (index >= 0 && index < arrayLength) {
            return index;
        } else {
            return -1; // Return -1 to indicate invalid index
        }
    }
}
