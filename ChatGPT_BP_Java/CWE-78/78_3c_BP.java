import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SecureCommandExecution {

    public static void main(String[] args) {
        String command = "ls";  // Default command
        executeCommand(command);
    }

    public static void executeCommand(String command) {
        // Input Validation: Check for null or empty command
        if (command == null || command.trim().isEmpty()) {
            System.err.println("Error: Command cannot be null or empty.");
            return;
        }

        // Input Sanitization: Allow only 'ls' command for security
        if (!command.trim().equals("ls")) {
            System.err.println("Error: Only 'ls' command is allowed.");
            return;
        }

        // Perform command execution
        try {
            Process process = Runtime.getRuntime().exec(command);
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("Output of the command:");

            // Reading output
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for the process to complete and check the exit value
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Error: Command execution failed with exit code " + exitCode);
            }

        } catch (IOException e) {
            System.err.println("IOException occurred: " + e.getMessage());
        } catch (InterruptedException e) {
            System.err.println("Command execution was interrupted: " + e.getMessage());
            Thread.currentThread().interrupt(); // Restore the interrupted status
        }
    }

    public static String print(String format, Object... args) {
        return String.format(format, args);
    }
}
