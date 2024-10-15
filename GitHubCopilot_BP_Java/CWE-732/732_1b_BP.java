package GitHubCopilot_BP_Java.CWE_732;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.attribute.PosixFilePermission;
import java.util.Set;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        String fileName = "important_config";
        String content = "important_config";
        Path filePath = Paths.get(fileName);
        
        // Define the file permissions
        Set<PosixFilePermission> perms = new HashSet<>();
        perms.add(PosixFilePermission.OWNER_READ);
        perms.add(PosixFilePermission.OWNER_WRITE);

        FileOutputStream fos = null;
        try {
            // Create the file with the specified permissions if it does not exist
            if (!Files.exists(filePath)) {
                Files.createFile(filePath);
                Files.setPosixFilePermissions(filePath, perms);
            }
            
            // Open the file for writing only
            fos = new FileOutputStream(fileName, false);
            fos.write(content.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}