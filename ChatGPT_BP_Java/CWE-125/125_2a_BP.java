import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    // Array id_sequence with some values
    private static final int[] id_sequence = {101, 102, 103, 104, 105};

    // Function to retrieve value at the specified index
    public static int getValueAtIndex(int index) {
        if (index < 0 || index >= id_sequence.length) {
            return -1;  // Error handling for out-of-bounds index
        }
        return id_sequence[index];
    }

    // Main function to prompt user for index and call the function
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            // Input validation and secure execution
            System.out.print("Enter an index value: ");
            int index = scanner.nextInt();

            // Call the function and retrieve value
            int result = getValueAtIndex(index);

            // Check if index was valid and print result
            if (result != -1) {
                System.out.println("Value at index " + index + ": " + result);
            } else {
                System.out.println("Error: Index out of bounds.");
            }
        } catch (InputMismatchException e) {
            // Handle invalid input (non-integer)
            System.out.println("Error: Please enter a valid integer.");
        } finally {
            // Clean up resources
            scanner.close();
        }
    }
}
