package GitHubCopilot_BP_Java.CWE_787;

public class Main {
    public static void main(String[] args) {
        // Validate command-line arguments
        if (args.length != 1) {
            System.err.println("Error: Please provide exactly one argument.");
            System.exit(1);
        }

        // Sanitize input by trimming whitespace
        String input = args[0].trim();

        // Output encoding: Print the sanitized input
        System.out.println(encodeForConsole(input));
    }

    // Method to encode output for console
    private static String encodeForConsole(String input) {
        // Simple encoding to prevent console injection attacks
        return input.replaceAll("[^\\p{Print}]", "");
    }
}