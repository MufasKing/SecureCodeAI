package GitHubCopilot_BP_Java.CWE_119;

public class Main {
    public static void main(String[] args) {
        // Validate the number of command line arguments
        if (args.length < 2) {
            System.err.println("Error: Not enough command line arguments.");
            System.exit(1);
        }

        int index;
        try {
            // Secure String-To-Integer Conversion
            index = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.err.println("Error: Second argument is not a valid integer.");
            System.exit(1);
            return; // This return is redundant but added for clarity
        }

        // Validate the range of the converted integer
        if (index < 0 || index >= args.length) {
            System.err.println("Error: Index out of range.");
            System.exit(1);
        }

        // Secure Output
        System.out.println(args[index]);

        // Exit the program
        System.exit(0);
    }
}