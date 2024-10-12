import java.io.*;
import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermission;
import java.util.HashSet;
import java.util.Set;

public class FileHandler {

    private static final String TEMP_FILE_PREFIX = "temp_";
    private static final String TEMP_FILE_SUFFIX = ".tmp";
    private static final String FILE_PATH = "important_config.txt"; // Replace with your desired file path

    public static void main(String[] args) {
        // Create a temporary file
        Path tempFile = null;
        try {
            tempFile = Files.createTempFile(TEMP_FILE_PREFIX, TEMP_FILE_SUFFIX);
            System.out.println("Temporary file created at: " + tempFile.toString());

            // Set file permissions (0700)
            Set<PosixFilePermission> perms = new HashSet<>();
            perms.add(PosixFilePermission.OWNER_READ);
            perms.add(PosixFilePermission.OWNER_WRITE);
            perms.add(PosixFilePermission.OWNER_EXECUTE);
            Files.setPosixFilePermissions(tempFile, perms);

            // Write data to the file
            writeFile(tempFile, "important_config");

            // Move the temporary file to the desired final location
            Files.move(tempFile, Paths.get(FILE_PATH), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File written and moved to: " + FILE_PATH);

        } catch (IOException e) {
            System.err.println("Error occurred: " + e.getMessage());
            // Handle exceptions such as file creation, permission issues, etc.
        } finally {
            // Clean up the temporary file if it still exists
            if (tempFile != null && Files.exists(tempFile)) {
                try {
                    Files.delete(tempFile);
                    System.out.println("Temporary file deleted.");
                } catch (IOException e) {
                    System.err.println("Failed to delete temporary file: " + e.getMessage());
                }
            }
        }
    }

    private static void writeFile(Path filePath, String data) throws IOException {
        // Secure data writing using BufferedWriter
        try (BufferedWriter writer = Files.newBufferedWriter(filePath)) {
            writer.write(data);
            System.out.println("Data written to temporary file.");
        } catch (IOException e) {
            System.err.println("Failed to write to the file: " + e.getMessage());
            throw e; // Re-throw to handle in the main method
        }
    }
}
