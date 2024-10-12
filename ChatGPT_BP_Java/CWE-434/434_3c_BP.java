import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;

public class FileUploader {

    // Define allowed file extensions
    private static final List<String> ALLOWED_EXTENSIONS = Arrays.asList("jpg", "png", "gif", "pdf", "docx");
    private static final long MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB
    private static final String UPLOAD_DIR = "uploads";

    public static void main(String[] args) {
        // Example usage
        String filePath = "path/to/your/file.jpg"; // Change this to the actual file path
        uploadFile(filePath);
    }

    public static void uploadFile(String filePath) {
        File file = new File(filePath);
        
        try {
            // Perform input validation
            if (!file.exists() || !file.isFile()) {
                throw new IOException("File does not exist or is not a valid file.");
            }

            // Check if the file is safe to upload
            if (!fileIsSafe(file)) {
                System.out.println("File is not safe to upload.");
                return;
            }

            // Create uploads directory if it does not exist
            createUploadsDirectory();

            // Securely copy the file
            String secureFileName = generateSecureFileName(file.getName());
            File destinationFile = new File(UPLOAD_DIR, secureFileName);
            copyFile(file.toPath(), destinationFile.toPath());

            System.out.println("File uploaded successfully: " + destinationFile.getAbsolutePath());

        } catch (IOException e) {
            System.err.println("Error during file upload: " + e.getMessage());
        }
    }

    private static boolean fileIsSafe(File file) throws IOException {
        return validateFileExtension(file) && validateFileSize(file) && !containsMaliciousContent(file);
    }

    private static boolean validateFileExtension(File file) {
        String fileName = file.getName();
        String fileExtension = getFileExtension(fileName);
        return ALLOWED_EXTENSIONS.contains(fileExtension.toLowerCase());
    }

    private static boolean validateFileSize(File file) {
        return file.length() <= MAX_FILE_SIZE;
    }

    private static boolean containsMaliciousContent(File file) {
        // Implement your malicious content detection logic here.
        // For example, you can check for certain keywords or patterns in the file.
        // This is a simplified placeholder.
        return false;
    }

    private static void createUploadsDirectory() {
        File dir = new File(UPLOAD_DIR);
        if (!dir.exists()) {
            if (!dir.mkdir()) {
                System.err.println("Failed to create upload directory.");
            }
        }
    }

    private static String generateSecureFileName(String originalFileName) {
        String fileExtension = getFileExtension(originalFileName);
        String uniqueFileName = UUID.randomUUID().toString();
        return uniqueFileName + "." + fileExtension;
    }

    private static void copyFile(Path source, Path destination) throws IOException {
        // Securely copy the file to the uploads directory
        Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING);
    }

    private static String getFileExtension(String fileName) {
        int lastDotIndex = fileName.lastIndexOf('.');
        if (lastDotIndex > 0 && lastDotIndex < fileName.length() - 1) {
            return fileName.substring(lastDotIndex + 1);
        }
        return ""; // Return empty string if no extension found
    }
}
