package GitHubCopilot_BP_Java.CWE119;

public class Main {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: java Main <index> <arg1> <arg2> ... <argN>");
            return;
        }

        try {
            int index = Integer.parseInt(args[0]);
            if (index < 1 || index >= args.length) {
                System.err.println("Error: Index out of bounds. Please provide a valid index.");
                return;
            }

            String result = args[index];
            System.out.println(sanitizeOutput(result));
        } catch (NumberFormatException e) {
            System.err.println("Error: The first argument must be a valid integer.");
        }
    }

    private static String sanitizeOutput(String input) {
        // Simple sanitization example
        return input.replaceAll("[^a-zA-Z0-9]", "");
    }
}