import java.util.InputMismatchException;
import java.util.Scanner;

public class SecureArrayAccess {

    // Example array for demonstration
    private static int[] id_sequence = {10, 20, 30, 40, 50};

    public static void main(String[] args) {
        // Call the function and capture the return value
        int result = getValueAtIndex();

        // Handle the return value (optional depending on how you want to use it)
        if (result == 0) {
            System.out.println("Program executed successfully.");
        }
    }

    public static int getValueAtIndex() {
        Scanner scanner = new Scanner(System.in);
        int index = -1;  // Initialize with an invalid value for safety

        try {
            // Prompt user for input
            System.out.print("Enter an index value: ");
            index = scanner.nextInt();

            // Validate that the index is within the bounds of the array
            if (index < 0 || index >= id_sequence.length) {
                System.out.println("Error: Index out of bounds.");
                return -1;
            }

            // Return the value at the specified index
            System.out.println("Value at index " + index + ": " + id_sequence[index]);
            return id_sequence[index];

        } catch (InputMismatchException e) {
            System.out.println("Error: Invalid input. Please enter a valid integer.");
            return -1;  // Error code for invalid input
        } catch (Exception e) {
            // Catch any unforeseen errors and handle them
            System.out.println("An unexpected error occurred: " + e.getMessage());
            return -1;
        } finally {
            // Ensure scanner is closed properly to avoid resource leak
            scanner.close();
        }
    }
}

