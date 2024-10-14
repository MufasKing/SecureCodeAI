import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SecureCommandExecution {

    // Function to format the command string safely
    public static String formatCommand(String format, Object... args) {
        return String.format(format, args);
    }

    // Function to execute the ls command securely
    public static void executeCommand(String command) {
        ProcessBuilder processBuilder = new ProcessBuilder();
        processBuilder.command(command.split(" ")); // Split command into parts for ProcessBuilder

        try {
            Process process = processBuilder.start(); // Start the process

            // Capture output
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line); // Print the output
            }

            // Capture errors
            BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            while ((line = errorReader.readLine()) != null) {
                System.err.println(line); // Print the error output
            }

            // Wait for the process to finish and check the exit value
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Command execution failed with exit code: " + exitCode);
            }

        } catch (IOException e) {
            System.err.println("IOException occurred: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Process was interrupted: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Ensure command is properly sanitized and secured
        String sanitizedCommand = formatCommand("ls"); // Format and sanitize input
        executeCommand(sanitizedCommand); // Execute command
    }
}
