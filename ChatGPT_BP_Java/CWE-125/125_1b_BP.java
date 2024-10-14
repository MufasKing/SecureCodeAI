import java.util.Scanner;

public class Main {
    
    // Function to get the value from the array if the index is valid
    public static int getValueFromArray(int[] array, int size, int index) {
        // Input validation for array bounds
        if (index >= 0 && index < size) {
            return array[index];
        } else {
            // Return -1 if index is out of bounds
            return -1;
        }
    }

    // Function to safely read an integer input from the user
    public static int getInput(Scanner scanner) {
        System.out.print("Enter an index: ");
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid integer.");
            scanner.next(); // Clear the invalid input
        }
        return scanner.nextInt();
    }

    // Main function
    public static void main(String[] args) {
        // Example array
        int[] id_sequence = {10, 20, 30, 40, 50};
        int size = id_sequence.length;

        // Secure input reading with validation
        Scanner scanner = new Scanner(System.in);
        int index = getInput(scanner);

        // Error handling for array access
        int result = getValueFromArray(id_sequence, size, index);

        // Return the result as the exit code
        System.exit(result);
    }
}
