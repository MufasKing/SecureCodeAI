public class ArgumentHandler {

    public static void main(String[] args) {
        // Check if exactly one argument is provided
        if (args.length != 1) {
            System.err.println("Error: Exactly one argument is required.");
            System.exit(1); // Exit with an error code
        }

        // Safely retrieve the input argument
        String input = args[0];

        // Print the original argument
        System.out.println("Original argument: \"" + input + "\"");

        // Trim trailing whitespace from the argument
        String trimmedInput = input.trim();

        // Print the trimmed argument
        System.out.println("Trimmed argument: \"" + trimmedInput + "\"");

        // Exit the program gracefully
        System.exit(0);
    }
}
