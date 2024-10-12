public class HexStringValidator {
    public static void main(String[] args) {
        // Check if exactly one argument is provided
        if (args.length != 1) {
            System.err.println("Error: Exactly one argument is required.");
            System.exit(1);
        }

        // Get the input string
        String input = args[0];

        // Validate that the string is a hex string
        if (!isHexString(input)) {
            System.err.println("Error: The provided string is not a valid hexadecimal string.");
            System.exit(1);
        }

        // Trim trailing whitespace
        input = trimTrailingWhitespace(input);

        // Trim newlines
        input = trimNewlines(input);

        // Null terminate the string (not typically done in Java, but for demonstration)
        input = input + '\0';

        // Output the validated and sanitized string
        System.out.println("Validated and sanitized hex string: " + input);
    }

    // Method to check if the string is a valid hex string
    private static boolean isHexString(String str) {
        // Regex to check if the string is a hex string
        return str.matches("^[0-9a-fA-F]+$");
    }

    // Method to trim trailing whitespace
    private static String trimTrailingWhitespace(String str) {
        return str.replaceAll("\\s+$", "");
    }

    // Method to trim newlines
    private static String trimNewlines(String str) {
        return str.replaceAll("[\\r\\n]+$", "");
    }
}
