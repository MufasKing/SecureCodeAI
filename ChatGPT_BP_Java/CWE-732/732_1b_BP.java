import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermissions;
import java.io.IOException;

public class ImportantConfigWriter {
    private static final String FILE_NAME = "important_config";
    private static final String CONTENT = "important_config";

    public static void main(String[] args) {
        // Create a Path object for the file
        Path path = Paths.get(FILE_NAME);

        // Define file permissions: owner can read and write
        String permissions = "rw-------"; // S_IRUSR | S_IWUSR
        try {
            // Create the file if it doesn't exist, with specified permissions
            if (!Files.exists(path)) {
                Files.createFile(path, PosixFilePermissions.asFileAttribute(PosixFilePermissions.fromString(permissions)));
            }

            // Write to the file (open in write-only mode)
            Files.write(path, CONTENT.getBytes(), StandardOpenOption.WRITE);

            System.out.println("Content written to the file successfully.");
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            // Closing resources if any were opened (not necessary in this case since we use Files API)
            // This is just a placeholder to show where you would close resources if needed.
            // In real applications, you'd handle streams or channels that require explicit closing.
        }
    }
}
