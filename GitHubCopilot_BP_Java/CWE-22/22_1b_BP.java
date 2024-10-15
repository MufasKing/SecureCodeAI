package GitHubCopilot_BP_Java.CWE_22;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    private static final String BASE_DIRECTORY = "/safe/";

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Main <filename>");
            return;
        }

        String requestedFile = args[0];
        readFile(requestedFile);
    }

    public static void readFile(String fileName) {
        try {
            Path basePath = Paths.get(BASE_DIRECTORY).toRealPath();
            Path requestedPath = basePath.resolve(fileName).normalize();

            // Validate that the requested file is within the base directory
            if (!requestedPath.startsWith(basePath)) {
                throw new SecurityException("Invalid file path");
            }

            // Read the file securely
            File file = requestedPath.toFile();
            if (file.exists() && file.isFile()) {
                String content = new String(Files.readAllBytes(requestedPath));
                System.out.println(content);
            } else {
                System.out.println("File not found or is not a regular file");
            }
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file");
        } catch (SecurityException e) {
            System.out.println("Access denied: " + e.getMessage());
        }
    }
}