import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermission;
import java.util.EnumSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Path filePath = Paths.get("important_config");

        // Set file permissions: readable and writable by the owner
        Set<PosixFilePermission> permissions = EnumSet.of(
                PosixFilePermission.OWNER_READ,
                PosixFilePermission.OWNER_WRITE
        );

        // Define file attributes
        FileAttribute<Set<PosixFilePermission>> fileAttributes = PosixFilePermissions.asFileAttribute(permissions);

        // Define file open options
        OpenOption[] options = {
                StandardOpenOption.CREATE,
                StandardOpenOption.TRUNCATE_EXISTING,
                StandardOpenOption.WRITE
        };

        // Open the file with the specified flags and permissions
        try (FileChannel fileChannel = FileChannel.open(filePath, options)) {
            // File is opened successfully
            System.out.println("File opened successfully with specified permissions and flags.");
        } catch (IOException e) {
            // Handle exceptions
            System.err.println("Error occurred while handling the file: " + e.getMessage());
        }
    }
}