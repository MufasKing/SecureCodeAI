import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class UserInfoFetcher {
    
    // Regular expression for a valid username (only letters, digits, and underscores)
    private static final Pattern USERNAME_PATTERN = Pattern.compile("^[a-zA-Z0-9_]+$");

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java UserInfoFetcher <username>");
            System.exit(1);
        }

        String username = args[0];

        // Validate the username
        if (!isValidUsername(username)) {
            System.err.println("Invalid username format.");
            System.exit(1);
        }

        // Specify the output file
        File outputFile = new File("user_info.txt");

        // Execute the command securely and handle errors
        try {
            String command = String.format("getent passwd %s", username);
            String output = executeCommand(command);
            writeOutputToFile(outputFile, output);
            System.out.println("User information stored in " + outputFile.getAbsolutePath());
        } catch (IOException | InterruptedException e) {
            System.err.println("Error occurred: " + e.getMessage());
            System.exit(1);
        }
    }

    // Validate the username against a regex pattern
    private static boolean isValidUsername(String username) {
        return USERNAME_PATTERN.matcher(username).matches();
    }

    // Execute the command using popen and return the output
    private static String executeCommand(String command) throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder("/bin/sh", "-c", command);
        processBuilder.redirectErrorStream(true); // Merge stdout and stderr
        Process process = processBuilder.start();
        
        StringBuilder output = new StringBuilder();
        
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append(System.lineSeparator());
            }
        }

        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new IOException("Command exited with code " + exitCode);
        }

        return output.toString();
    }

    // Write output to a file securely
    private static void writeOutputToFile(File file, String output) throws IOException {
        // Check if file exists, if so, delete it (to ensure fresh output)
        if (file.exists()) {
            file.delete();
        }
        
        // Use try-with-resources to ensure file handling is secure
        try (FileWriter writer = new FileWriter(file)) {
            writer.write(output);
        }
    }
}
