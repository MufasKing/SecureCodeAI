import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class Main {

    // Method to sanitize the input username
    private static String sanitizeUsername(String username) {
        if (username == null || username.isEmpty()) {
            throw new IllegalArgumentException("Username cannot be null or empty");
        }
        // Allow only alphanumeric characters and underscores
        if (!Pattern.matches("^[a-zA-Z0-9_]+$", username)) {
            throw new IllegalArgumentException("Invalid username format");
        }
        return username;
    }

    // Method to execute the command and write output to a file
    private static void executeCommand(String username) {
        String sanitizedUsername = sanitizeUsername(username);
        String command = "getent passwd " + sanitizedUsername;
        ProcessBuilder processBuilder = new ProcessBuilder("sh", "-c", command);
        processBuilder.redirectErrorStream(true);

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(processBuilder.start().getInputStream()));
             FileWriter writer = new FileWriter("output.txt", false)) {
            String line;
            while ((line = reader.readLine()) != null) {
                writer.write(line + System.lineSeparator());
            }
        } catch (IOException e) {
            System.err.println("An error occurred while executing the command: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Main <username>");
            System.exit(1);
        }
        executeCommand(args[0]);
    }
}