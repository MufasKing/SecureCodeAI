package GitHubCopilot_BP_Java.CWE_787;

public class Main {
    public static void main(String[] args) {
        // Handling command-line arguments
        if (args.length != 1) {
            System.err.println("Error: Exactly one argument is required.");
            System.exit(1);
        }

        String input = args[0];

        // Input validation: Check if the string is a hex string
        if (!input.matches("^[0-9A-Fa-f]+$")) {
            System.err.println("Error: Argument must be a hex string.");
            System.exit(1);
        }

        // Input sanitization: Trim trailing whitespace
        int end = input.length();
        for (int i = input.length() - 1; i >= 0; i--) {
            if (!Character.isWhitespace(input.charAt(i))) {
                end = i + 1;
                break;
            }
        }
        input = input.substring(0, end);

        // Input sanitization: Trim newlines
        int start = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) != '\n') {
                start = i;
                break;
            }
        }
        input = input.substring(start, end);

        // Null terminate the string
        input += '\0';

        // Output the sanitized string
        System.out.println("Sanitized input: " + input);
    }
}