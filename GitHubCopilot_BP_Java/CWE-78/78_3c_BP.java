package GitHubCopilot_BP_Java.CWE_78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String command = "ls";
        executeCommand(command);
    }

    public static void executeCommand(String command) {
        // Input Validation
        if (command == null || command.trim().isEmpty()) {
            System.out.println("Invalid command");
            return;
        }

        // Input Sanitization
        command = command.replaceAll("[^a-zA-Z0-9\\s]", "");

        // Secure Command Execution
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
            System.out.println("\nExited with code: " + exitCode);
        } catch (IOException e) {
            System.err.println("IOException occurred: " + e.getMessage());
        } catch (InterruptedException e) {
            System.err.println("InterruptedException occurred: " + e.getMessage());
            Thread.currentThread().interrupt();
        }
    }
}