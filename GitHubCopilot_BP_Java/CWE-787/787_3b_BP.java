package GitHubCopilot_BP_Java.CWE-787;

public class Main {
    public static void main(String[] args) {
        // Argument Validation
        if (args.length != 1) {
            System.err.println("Error: Exactly one argument is required.");
            System.exit(1);
        }

        // Input Retrieval
        String input = args[0];

        // Output Handling
        System.out.println("Original input: " + input);

        // Trailing Whitespace Trimming
        input = input.trim();

        // Output Handling
        System.out.println("Trimmed input: " + input);

        // Exit the program
        System.exit(0);
    }
}