public class CommandLineArgumentPrinter {

    public static void main(String[] args) {
        try {
            validateInput(args);
            String sanitizedInput = sanitizeInput(args[0]);
            printOutput(sanitizedInput);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }

    // Validates the command line arguments
    private static void validateInput(String[] args) {
        if (args.length != 1) {
            throw new IllegalArgumentException("Exactly one command line argument is required.");
        }
    }

    // Sanitizes the input by trimming whitespace and handling special characters
    private static String sanitizeInput(String input) {
        if (input == null) {
            throw new IllegalArgumentException("Input cannot be null.");
        }
        // Trim trailing whitespace
        String trimmedInput = input.trim();
        // Further sanitization can be added here as needed
        return trimmedInput;
    }

    // Prints the sanitized output to the console
    private static void printOutput(String output) {
        // Output encoding can be implemented if necessary
        System.out.println("Output: " + encodeOutput(output));
    }

    // Encodes output to prevent XSS or other vulnerabilities if the output is displayed in a web context
    private static String encodeOutput(String output) {
        return output.replace("&", "&amp;")
                     .replace("<", "&lt;")
                     .replace(">", "&gt;")
                     .replace("\"", "&quot;")
                     .replace("'", "&apos;");
    }
}
