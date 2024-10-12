import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.nio.file.attribute.PosixFilePermissions;

public class ImportantConfig {

    public static void main(String[] args) {
        String fileName = "important_config";
        Path path = Path.of(fileName);

        // Create the file with specific permissions
        try {
            // Create the file if it doesn't exist; truncate if it does
            Files.writeString(path, "", StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);

            // Set file permissions (owner read/write)
            Files.setPosixFilePermissions(path, PosixFilePermissions.fromString("rw-------"));

            System.out.println("File created successfully with specified permissions.");

        } catch (IOException e) {
            System.err.println("Error occurred while creating the file: " + e.getMessage());
        } finally {
            // Close any resources if necessary (none open in this case)
            System.out.println("Finished processing.");
        }
    }
}
