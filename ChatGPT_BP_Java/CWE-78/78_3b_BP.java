import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class CommandExecutor {

    public static void main(String[] args) {
        // Example usage
        String path = "/path/to/directory"; // Specify the directory path
        String command = print("ls %s", path);
        executeCommand(command);
    }

    // Function to create formatted command string
    public static String print(String format, Object... args) {
        return String.format(format, args);
    }

    // Function to execute command
    public static void executeCommand(String command) {
        // Input validation and sanitization
        if (!isValidCommand(command)) {
            System.err.println("Invalid command.");
            return;
        }

        // Split the command into a command array for ProcessBuilder
        String[] commandArray = command.split(" ");

        // Using ProcessBuilder for secure subprocess execution
        ProcessBuilder processBuilder = new ProcessBuilder(commandArray);
        processBuilder.redirectErrorStream(true); // Combine stderr and stdout

        try {
            // Start the process
            Process process = processBuilder.start();

            // Read the output of the command
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }

            // Wait for the process to complete and check the exit value
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Command exited with error code: " + exitCode);
            }
        } catch (IOException | InterruptedException e) {
            System.err.println("An error occurred while executing the command: " + e.getMessage());
            Thread.currentThread().interrupt(); // Restore interrupted status
        }
    }

    // Function to validate the command (simple example)
    private static boolean isValidCommand(String command) {
        // Allow only safe commands (you can implement more sophisticated checks)
        String[] allowedCommands = {"ls"};
        String cmd = command.split(" ")[0];
        return Arrays.asList(allowedCommands).contains(cmd);
    }
}
