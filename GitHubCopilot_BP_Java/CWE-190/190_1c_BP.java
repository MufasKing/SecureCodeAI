public class AddValue {
    public static void main(String[] args) {
        // Ensure only one argument is passed
        if (args.length != 1) {
            System.err.println("Error: Please provide exactly one integer argument.");
            System.exit(1);
        }

        try {
            // Secure input conversion
            int inputValue = Integer.parseInt(args[0]);

            // Add 1000 to the input value
            int result = addThousand(inputValue);

            // Print the result
            System.out.println("Result: " + result);

            // Explicit exit with 0
            System.exit(0);
        } catch (NumberFormatException e) {
            System.err.println("Error: Invalid input. Please provide a valid integer.");
            System.exit(1);
        }
    }

    // Separation of concerns: method to add 1000 to the input value
    private static int addThousand(final int value) {
        return value + 1000;
    }
}