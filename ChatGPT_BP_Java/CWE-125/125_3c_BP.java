import java.util.Scanner;

public class ArrayLookup {

    // Method to get the value at a specific index
    public static int getValueAtIndex(int[] arr, int index) {
        try {
            // Check if the index is within bounds
            if (index >= 0 && index < arr.length) {
                return arr[index];
            } else {
                // Return -1 if the index is out of bounds
                return -1;
            }
        } catch (Exception e) {
            // Handle any unexpected exceptions
            System.out.println("An unexpected error occurred: " + e.getMessage());
            return -1;
        }
    }

    // Method to validate the user input
    public static int getValidInput(Scanner scanner) {
        int input;
        while (true) {
            System.out.print("Enter an index: ");
            if (scanner.hasNextInt()) {
                input = scanner.nextInt();
                break;
            } else {
                System.out.println("Invalid input. Please enter a valid integer.");
                scanner.next();  // Clear invalid input
            }
        }
        return input;
    }

    public static void main(String[] args) {
        // Example array
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

        // Create a scanner object to get user input
        Scanner scanner = new Scanner(System.in);

        // Get validated input from user
        int index = getValidInput(scanner);

        // Retrieve the value at the input index
        int value = getValueAtIndex(arr, index);

        // Output the result
        if (value != -1) {
            System.out.println("Value at index " + index + " is: " + value);
        } else {
            System.out.println("Index out of bounds, returning: -1");
        }

        // Close the scanner
        scanner.close();
    }
}
