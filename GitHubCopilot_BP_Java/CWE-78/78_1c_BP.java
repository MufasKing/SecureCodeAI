package GitHubCopilot_BP_Java.CWE_78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Main <username>");
            System.exit(1);
        }

        String username = args[0];

        // Input Validation
        if (!isValidUsername(username)) {
            System.err.println("Invalid username.");
            System.exit(1);
        }

        // Execute the command securely
        int exitStatus = runCommand(username);

        // Print the exit status
        System.out.println("Command exit status: " + exitStatus);
    }

    private static boolean isValidUsername(String username) {
        // Validate username (e.g., only alphanumeric and underscores)
        return username.matches("[a-zA-Z0-9_]+");
    }

    private static int runCommand(String username) {
        ProcessBuilder processBuilder = new ProcessBuilder("id", username);
        processBuilder.redirectErrorStream(true);

        try {
            Process process = processBuilder.start();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
            return process.waitFor();
        } catch (IOException | InterruptedException e) {
            System.err.println("Error executing command: " + e.getMessage());
            return -1;
        }
    }
}