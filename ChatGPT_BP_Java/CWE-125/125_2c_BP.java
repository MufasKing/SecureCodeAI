import java.util.Scanner;

public class ArrayLookup {

    // Array containing some example values
    private static final int[] id_sequence = {10, 20, 30, 40, 50};

    public static void main(String[] args) {
        // Call the function and print the result
        System.out.println("Value at the given index: " + getValueAtIndex());
    }

    // Function to get value from id_sequence based on user input index
    public static int getValueAtIndex() {
        Scanner scanner = null;
        try {
            // Using the least privilege principle: limit scanner usage inside try block
            scanner = new Scanner(System.in);

            // Prompt user for input
            System.out.print("Enter an index: ");
            String input = scanner.nextLine();

            // Validate input: check if the input is an integer
            int index = validateAndParseInput(input);

            // Perform bounds checking
            if (index >= 0 && index < id_sequence.length) {
                return id_sequence[index];  // Return the value if index is valid
            } else {
                System.out.println("Index out of bounds. Returning 0.");
                return 0;  // Return 0 if the index is out of bounds
            }

        } catch (NumberFormatException e) {
            // Handle invalid input format (non-integer input)
            System.out.println("Invalid input. Please enter a valid integer.");
            return 0;
        } finally {
            // Ensure that the scanner is closed properly
            if (scanner != null) {
                scanner.close();
            }
        }
    }

    // Helper method to validate and parse the input into an integer
    private static int validateAndParseInput(String input) throws NumberFormatException {
        return Integer.parseInt(input);  // Throws NumberFormatException if input is not an integer
    }
}

