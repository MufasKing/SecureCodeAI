package GitHubCopilot_BP_Java.CWE_78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        String command = print("ls");
        executeCommand(command);
    }

    public static String print(String format, Object... args) {
        return String.format(format, args);
    }

    public static void executeCommand(String command) {
        // Input Sanitization
        if (command == null || command.trim().isEmpty()) {
            System.out.println("Invalid command");
            return;
        }

        // Secure Subprocess Execution
        ProcessBuilder processBuilder = new ProcessBuilder();
        processBuilder.command("sh", "-c", command);

        try {
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.out.println("Error: Command execution failed with exit code " + exitCode);
            }
        } catch (IOException | InterruptedException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}