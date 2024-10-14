package GitHubCopilot_BP_Java.CWE-119;

public class Main {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Main <number1> <number2> ... <numberN>");
            return;
        }

        for (int i = 1; i < args.length; i++) {
            String arg = args[i];
            try {
                // Input validation and sanitization
                if (!arg.matches("-?\\d+")) {
                    throw new NumberFormatException("Invalid integer format: " + arg);
                }

                // Robust integer conversion
                int number = Integer.parseInt(arg);

                // Output formatting
                System.out.printf("Argument %d: %d%n", i, number);
            } catch (NumberFormatException e) {
                System.err.println("Error converting argument " + i + ": " + e.getMessage());
            } catch (Exception e) {
                System.err.println("Unexpected error: " + e.getMessage());
            }
        }
    }
}