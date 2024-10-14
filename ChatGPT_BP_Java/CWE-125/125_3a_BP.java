import java.util.Scanner;

public class SecureArrayAccess {

    public static void main(String[] args) {
        // Define the array
        int[] array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        
        // Get user input
        int index = getInput();
        
        // Perform bounds checking and return value or error
        int result = getValueAtIndex(array, index);
        System.out.println("Result: " + result);
    }

    /**
     * This method securely retrieves user input and validates it.
     */
    private static int getInput() {
        Scanner scanner = new Scanner(System.in);
        int input = -1;
        boolean isValid = false;
        
        while (!isValid) {
            try {
                System.out.print("Enter an integer index: ");
                String userInput = scanner.nextLine().trim();
                
                // Validate the string input and convert it to an integer
                input = Integer.parseInt(userInput);
                
                isValid = true; // Valid input
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid integer.");
            }
        }
        
        scanner.close(); // Close scanner to prevent resource leak
        return input;
    }

    /**
     * This method retrieves the value at a given index from the array securely.
     * It handles invalid inputs and out-of-bounds accesses.
     */
    private static int getValueAtIndex(int[] array, int index) {
        // Input validation and bounds checking
        if (index < 0 || index >= array.length) {
            return -1; // Return -1 if the index is out of bounds or invalid
        }
        
        try {
            return array[index]; // Return the value at the given index
        } catch (ArrayIndexOutOfBoundsException e) {
            // This shouldn't occur due to bounds checking but catch just in case
            System.err.println("Error: Index out of bounds.");
            return -1;
        }
    }
}
