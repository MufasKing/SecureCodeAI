import java.util.InputMismatchException;
import java.util.Scanner;

public class ArrayHandler {

    // Encapsulated array (private)
    private int[] numbersArray = {10, 20, 30, 40, 50};

    // Method to get value at the given index
    public int getValueAtIndex(int index) {
        // Index Validation and Bounds Checking
        if (index < 0 || index >= numbersArray.length) {
            System.out.println("Error: Index out of bounds.");
            return -1;
        }
        return numbersArray[index];
    }

    // Method to handle input from the user and sanitize it
    public void handleUserInput() {
        Scanner scanner = new Scanner(System.in);
        int index = -1;

        try {
            System.out.print("Enter an index: ");
            index = scanner.nextInt(); // Input Validation: ensures an integer is entered
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
            return;
        } finally {
            scanner.nextLine(); // Clean up the scanner buffer
        }

        // Get value at the sanitized index
        int result = getValueAtIndex(index);

        // Output the result
        if (result != -1) {
            System.out.println("Value at index " + index + ": " + result);
        }
    }

    public static void main(String[] args) {
        ArrayHandler handler = new ArrayHandler();
        handler.handleUserInput();
    }
}
