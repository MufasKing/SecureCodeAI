import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class UserIdCommand {
    // Regular expression to validate usernames
    private static final Pattern USERNAME_PATTERN = Pattern.compile("^[a-zA-Z0-9._-]{3,16}$");

    public static void main(String[] args) {
        // Check if a username is provided
        if (args.length != 1) {
            System.err.println("Usage: java UserIdCommand <username>");
            System.exit(1);
        }

        String username = args[0];

        // Validate and sanitize the username input
        if (!isValidUsername(username)) {
            System.err.println("Invalid username. It must be 3 to 16 characters long and can only contain letters, digits, dots, underscores, or hyphens.");
            System.exit(1);
        }

        // Execute the command and get the exit status
        int exitStatus = executeCommand(username);
        System.out.println("Exit Status: " + exitStatus);
    }

    // Function to validate the username
    private static boolean isValidUsername(String username) {
        return USERNAME_PATTERN.matcher(username).matches();
    }

    // Function to execute the 'id' command
    private static int executeCommand(String username) {
        ProcessBuilder processBuilder = new ProcessBuilder("id", username);
        processBuilder.redirectErrorStream(true); // Combine stdout and stderr

        int exitStatus = -1; // Default exit status for error
        try {
            Process process = processBuilder.start();

            // Read the output from the command
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line); // Print the output safely
                }
            }

            // Wait for the process to finish and get the exit status
            exitStatus = process.waitFor();
        } catch (IOException e) {
            System.err.println("IOException occurred: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Restore the interrupted status
            System.err.println("Command execution interrupted: " + e.getMessage());
        }

        return exitStatus;
    }
}
