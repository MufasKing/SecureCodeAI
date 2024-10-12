import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermission;
import java.util.HashSet;
import java.util.Set;

public class SecureFileHandling {

    public static void main(String[] args) {
        String filePath = "important_config";
        String contentToWrite = "important_config";
        
        try {
            // Create the file if it doesn't exist with specified permissions
            Path path = Paths.get(filePath);
            if (!Files.exists(path)) {
                Set<PosixFilePermission> permissions = new HashSet<>();
                permissions.add(PosixFilePermission.OWNER_READ);
                permissions.add(PosixFilePermission.OWNER_WRITE);
                permissions.add(PosixFilePermission.GROUP_READ);
                permissions.add(PosixFilePermission.OTHERS_READ);
                
                // Create the file with the specified permissions
                Files.createFile(path);
                Files.setPosixFilePermissions(path, permissions);
                System.out.println("File created with permissions: " + permissions);
            }

            // Write the content to the file
            Files.write(path, contentToWrite.getBytes(), StandardOpenOption.WRITE);
            System.out.println("Content written to file: " + contentToWrite);
            
        } catch (FileAlreadyExistsException e) {
            System.err.println("Error: The file already exists: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error: Unable to open or write to the file: " + e.getMessage());
        } catch (UnsupportedOperationException e) {
            System.err.println("Error: POSIX file permissions not supported: " + e.getMessage());
        }
    }
}
