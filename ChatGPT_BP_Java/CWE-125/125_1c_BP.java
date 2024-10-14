import java.util.Scanner;

public class Main {

    // Function to safely retrieve a value from the array
    public static int getValueFromArray(int[] array, int size, int index) {
        if (index >= 0 && index < size) {
            return array[index];
        } else {
            return -1;  // Return -1 if the index is out of bounds
        }
    }

    // Main function to read input, validate and handle exceptions
    public static void main(String[] args) {
        // Example array to retrieve values from
        int[] id_sequence = {10, 20, 30, 40, 50};
        int size = id_sequence.length;
        Scanner scanner = null;

        try {
            // Use Scanner in a try-with-resources block to automatically close it
            scanner = new Scanner(System.in);

            System.out.println("Please enter an integer index:");
            if (!scanner.hasNextInt()) {
                System.err.println("Invalid input. Please enter an integer.");
                System.exit(-1);  // Exit with -1 in case of invalid input
            }

            int index = scanner.nextInt();

            // Call the getValueFromArray function
            int result = getValueFromArray(id_sequence, size, index);

            // Exit with the result as the exit code
            System.exit(result);
        } catch (Exception e) {
            // Generic exception handling to cover unexpected errors
            System.err.println("An error occurred: " + e.getMessage());
            System.exit(-1);  // Exit with -1 in case of any exception
        } finally {
            // Ensure the scanner is closed if it was initialized
            if (scanner != null) {
                scanner.close();
            }
        }
    }
}
