import java.io.*;
import java.nio.file.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class SecureFileReader {
    private static final Logger LOGGER = Logger.getLogger(SecureFileReader.class.getName());
    private static final String SAFE_DIRECTORY = System.getProperty("user.home") + "/safe/";

    public static void main(String[] args) {
        // Example file name to read, could be supplied by user
        String requestedFileName = "example.txt"; // Replace with actual input
        readFile(requestedFileName);
    }

    public static void readFile(String fileName) {
        // Validate the file path to prevent directory traversal attacks
        Path filePath = Paths.get(SAFE_DIRECTORY, fileName).normalize();

        // Check if the resolved path is within the safe directory
        if (!filePath.startsWith(SAFE_DIRECTORY)) {
            LOGGER.log(Level.WARNING, "Access to the file {0} is denied. Invalid path.", fileName);
            System.out.println("Access denied.");
            return;
        }

        // Attempt to read the file
        try (BufferedReader reader = Files.newBufferedReader(filePath)) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line); // Process the line as needed
            }
        } catch (NoSuchFileException e) {
            LOGGER.log(Level.SEVERE, "File not found: {0}", filePath);
            System.out.println("File not found.");
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error reading file: {0}", filePath);
            System.out.println("An error occurred while reading the file.");
        }
    }
}
