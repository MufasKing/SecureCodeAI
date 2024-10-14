public class ArgvIndex {

    public static void main(String[] args) {
        // Ensure input validation is done
        if (args.length == 0) {
            System.err.println("Error: No command line arguments provided.");
            System.exit(1);
        }

        // Prompt user to enter an index
        try {
            int index = getIndexFromArgs(args);
            validateIndex(index, args.length);
            printArgumentAtIndex(index, args);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        } catch (NumberFormatException e) {
            System.err.println("Error: Invalid index format. Please provide a valid integer.");
            System.exit(1);
        }
    }

    // Separating the logic of parsing and validating the index
    private static int getIndexFromArgs(String[] args) throws NumberFormatException {
        // Convert the first argument to an integer
        return Integer.parseInt(args[0]);
    }

    // Ensure the index is within bounds
    private static void validateIndex(int index, int length) {
        // Check if index is positive and within the valid range
        if (index < 1 || index >= length) {
            throw new IllegalArgumentException("Index out of bounds. Please provide an index between 1 and " + (length - 1));
        }
    }

    // Logic for printing the argument at the given index
    private static void printArgumentAtIndex(int index, String[] args) {
        // Print securely to avoid injection attacks
        String argument = args[index];
        System.out.println("Argument at index " + index + ": " + escapeForOutput(argument));
    }

    // Securely escape the argument to avoid issues with special characters
    private static String escapeForOutput(String input) {
        // Basic escaping to prevent issues with special characters
        return input.replaceAll("[^\\w\\s]", "");
    }
}
