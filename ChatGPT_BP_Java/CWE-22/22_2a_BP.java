import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;

@Controller
public class ImageController {

    // Define allowed file types
    private static final String[] ALLOWED_EXTENSIONS = { "jpg", "jpeg", "png", "gif" };

    @GetMapping("/img")
    public ResponseEntity<byte[]> img(@RequestParam String name) {
        // Input Sanitization: Remove any unsafe characters
        String sanitizedFilename = sanitizeInput(name);
        
        // Validate file type
        if (!isValidFileType(sanitizedFilename)) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                                 .body("Invalid file type.".getBytes());
        }

        // Construct the file path
        File imageFile = new File("images/" + sanitizedFilename);
        
        // Error Handling: Check if the file exists
        if (!imageFile.exists()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                                 .body("File not found.".getBytes());
        }

        try (InputStream inputStream = new FileInputStream(imageFile)) {
            // Read the file content into a byte array
            byte[] imageBytes = inputStream.readAllBytes();
            return ResponseEntity.ok()
                                 .contentType(Files.probeContentType(imageFile.toPath()))
                                 .body(imageBytes);
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                 .body("Error reading file.".getBytes());
        }
    }

    private String sanitizeInput(String input) {
        // Basic sanitization: Allow only alphanumeric characters and dots
        return input.replaceAll("[^a-zA-Z0-9\\.]", "");
    }

    private boolean isValidFileType(String filename) {
        // Check file extension
        for (String extension : ALLOWED_EXTENSIONS) {
            if (filename.toLowerCase().endsWith("." + extension)) {
                return true;
            }
        }
        return false;
    }
}
