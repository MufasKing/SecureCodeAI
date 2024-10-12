import java.io.*;
import java.nio.file.*;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Set;

public class ImageUploader {

    // Allowed file extensions
    private static final Set<String> ALLOWED_EXTENSIONS = Set.of("jpg", "jpeg", "png", "gif");
    private static final String UPLOAD_DIR = "uploads";
    private static final String ENCODED_DIR = "encoded";

    public static void main(String[] args) {
        // Example usage
        try {
            Path imagePath = Path.of("path_to_image");
            uploadImage(imagePath);
        } catch (Exception e) {
            System.err.println("Error uploading image: " + e.getMessage());
        }
    }

    public static void uploadImage(Path imagePath) throws IOException {
        // Step 1: Secure filename
        String originalFileName = imagePath.getFileName().toString();
        String fileExtension = getFileExtension(originalFileName).toLowerCase();

        // Step 2: Validate file extension
        if (!ALLOWED_EXTENSIONS.contains(fileExtension)) {
            throw new IOException("Invalid file extension.");
        }

        // Step 3: Generate a random and secure filename
        String secureFileName = generateRandomFilename(fileExtension);

        // Step 4: Create directories if not existing
        Path uploadDirPath = Paths.get(UPLOAD_DIR);
        Path encodedDirPath = Paths.get(ENCODED_DIR);
        Files.createDirectories(uploadDirPath);
        Files.createDirectories(encodedDirPath);

        // Step 5: Secure file handling - Copy the file to the upload directory
        Path uploadedFilePath = uploadDirPath.resolve(secureFileName);
        Files.copy(imagePath, uploadedFilePath, StandardCopyOption.REPLACE_EXISTING);

        // Step 6: Read the file content and encode it as Base64
        byte[] fileBytes = Files.readAllBytes(uploadedFilePath);
        String encodedImage = Base64.getEncoder().encodeToString(fileBytes);

        // Step 7: Write the encoded image to a new file in the encoded directory
        Path encodedFilePath = encodedDirPath.resolve(secureFileName + ".txt");
        try (BufferedWriter writer = Files.newBufferedWriter(encodedFilePath)) {
            writer.write(encodedImage);
        }

        System.out.println("Image uploaded and encoded successfully.");
    }

    // Utility method to generate a secure, random filename
    private static String generateRandomFilename(String extension) {
        SecureRandom random = new SecureRandom();
        String randomFilename = new java.math.BigInteger(130, random).toString(32);
        return randomFilename + "." + extension;
    }

    // Utility method to get the file extension
    private static String getFileExtension(String fileName) {
        int lastDotIndex = fileName.lastIndexOf('.');
        if (lastDotIndex == -1 || lastDotIndex == fileName.length() - 1) {
            return "";
        }
        return fileName.substring(lastDotIndex + 1);
    }
}
