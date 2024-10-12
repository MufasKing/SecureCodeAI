package GitHubCopilot_BP_Java.CWE_434;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.UUID;

public class Main {
    private static final String[] ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"};
    private static final String UPLOAD_DIR = "uploads/";
    private static final String ENCODED_DIR = "encoded/";

    public static void main(String[] args) {
        // Example usage
        try {
            uploadImage("example.jpg", new byte[]{/* image bytes */});
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void uploadImage(String originalFilename, byte[] imageBytes) throws IOException {
        // Check file extension
        String fileExtension = getFileExtension(originalFilename);
        if (!isAllowedExtension(fileExtension)) {
            throw new IOException("File type not allowed.");
        }

        // Generate secure random filename
        String randomFilename = UUID.randomUUID().toString() + "." + fileExtension;

        // Ensure upload and encoded directories exist
        Files.createDirectories(Paths.get(UPLOAD_DIR));
        Files.createDirectories(Paths.get(ENCODED_DIR));

        // Save the uploaded file
        File uploadedFile = new File(UPLOAD_DIR + randomFilename);
        try (FileOutputStream fos = new FileOutputStream(uploadedFile)) {
            fos.write(imageBytes);
        }

        // Encode the image to base64
        String encodedImage = Base64.getEncoder().encodeToString(imageBytes);

        // Save the encoded image
        File encodedFile = new File(ENCODED_DIR + randomFilename + ".txt");
        try (FileOutputStream fos = new FileOutputStream(encodedFile)) {
            fos.write(encodedImage.getBytes());
        }
    }

    private static String getFileExtension(String filename) {
        int lastIndexOfDot = filename.lastIndexOf('.');
        if (lastIndexOfDot == -1) {
            return "";
        }
        return filename.substring(lastIndexOfDot + 1).toLowerCase();
    }

    private static boolean isAllowedExtension(String extension) {
        for (String allowedExtension : ALLOWED_EXTENSIONS) {
            if (allowedExtension.equals(extension)) {
                return true;
            }
        }
        return false;
    }
}