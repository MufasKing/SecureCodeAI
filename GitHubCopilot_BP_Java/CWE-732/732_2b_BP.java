package GitHubCopilot_BP_Java.CWE-732;

import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.EnumSet;

public class Main {
    public static void main(String[] args) {
        Path filePath = Paths.get("example.txt");

        // Check for file existence
        if (Files.exists(filePath)) {
            System.out.println("File already exists.");
            return;
        }

        // Define file attributes for least privilege
        FileAttribute<Set<PosixFilePermission>> fileAttributes = PosixFilePermissions.asFileAttribute(
                PosixFilePermissions.fromString("rw-------"));

        // Open file in write mode with specified options
        try (BufferedWriter writer = Files.newBufferedWriter(filePath,
                EnumSet.of(StandardOpenOption.CREATE_NEW, StandardOpenOption.WRITE), fileAttributes)) {
            writer.write("Hello, World!");
            System.out.println("File created and written successfully.");
        } catch (FileAlreadyExistsException e) {
            System.err.println("File already exists and O_EXCL flag is set.");
        } catch (IOException e) {
            System.err.println("An I/O error occurred: " + e.getMessage());
        }
    }
}