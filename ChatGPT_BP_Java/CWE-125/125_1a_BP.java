import java.util.Scanner;

public class Main {

    // Function to get the value from array safely with bounds checking
    public static int getValueFromArray(int[] array, int size, int index) {
        if (index < 0 || index >= size) {
            // Index out of bounds, return -1
            return -1;
        }
        // Return the value at the specified index
        return array[index];
    }

    // Main function handling input, validation, and error handling
    public static void main(String[] args) {
        // Define the array
        int[] id_sequence = {10, 20, 30, 40, 50};
        int size = id_sequence.length;

        // Initialize scanner to read input
        Scanner scanner = new Scanner(System.in);
        int index = -1;

        try {
            // Read input and validate
            System.out.println("Enter an integer index:");
            if (!scanner.hasNextInt()) {
                System.err.println("Error: Input must be an integer.");
                System.exit(1);
            }
            index = scanner.nextInt();

            // Call the getValueFromArray function
            int result = getValueFromArray(id_sequence, size, index);

            // Set exit code based on result
            if (result == -1) {
                System.err.println("Error: Index out of bounds.");
                System.exit(1);
            }

            // Output the value and exit
            System.out.println("Value at index " + index + ": " + result);
            System.exit(result);
            
        } catch (Exception e) {
            // Handle any unexpected errors
            System.err.println("An unexpected error occurred: " + e.getMessage());
            System.exit(1);
        } finally {
            // Close resources
            scanner.close();
        }
    }
}
