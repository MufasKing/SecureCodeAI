package GitHubCopilot_BP_Java.CWE_434;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;
import java.util.List;

public class Main {

    private static final List<String> ALLOWED_EXTENSIONS = Arrays.asList("jpg", "png", "txt", "pdf");
    private static final long MAX_FILE_SIZE = 10485760; // 10 MB

    public static boolean fileIsSafeType(File file) {
        String fileName = file.getName();
        String fileExtension = getFileExtension(fileName);

        if (!ALLOWED_EXTENSIONS.contains(fileExtension)) {
            return false;
        }

        if (file.length() > MAX_FILE_SIZE) {
            return false;
        }

        // Add additional checks for malicious content if necessary
        // For example, scanning the file for known malware signatures

        return true;
    }

    public static void uploadFile(File file) throws IOException {
        if (file == null || !file.exists()) {
            throw new IllegalArgumentException("Invalid file.");
        }

        if (!fileIsSafeType(file)) {
            throw new SecurityException("File type is not allowed or file is too large.");
        }

        String sanitizedFileName = sanitizeFileName(file.getName());
        File destinationDir = new File("uploads");
        if (!destinationDir.exists()) {
            destinationDir.mkdirs();
        }

        File destinationFile = new File(destinationDir, sanitizedFileName);
        Files.copy(file.toPath(), destinationFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
    }

    private static String getFileExtension(String fileName) {
        int dotIndex = fileName.lastIndexOf('.');
        return (dotIndex == -1) ? "" : fileName.substring(dotIndex + 1).toLowerCase();
    }

    private static String sanitizeFileName(String fileName) {
        return fileName.replaceAll("[^a-zA-Z0-9\\.\\-]", "_");
    }

    public static void main(String[] args) {
        // Example usage
        try {
            File file = new File("path/to/your/file.txt");
            uploadFile(file);
            System.out.println("File uploaded successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}