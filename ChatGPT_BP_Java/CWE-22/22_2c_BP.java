import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;

@RestController
public class ImageController {

    @Value("${file.upload-dir}")
    private String uploadDir; // Directory where files are stored

    @GetMapping("/img")
    public ResponseEntity<byte[]> img(@RequestParam("file") String fileName) {
        // Input Validation: Check if the fileName parameter is provided
        if (fileName == null || fileName.trim().isEmpty()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("File parameter is required.".getBytes());
        }

        // Secure File Path: Ensure the file path is safe to avoid directory traversal
        File file = new File(uploadDir, fileName);
        if (!file.getCanonicalPath().startsWith(new File(uploadDir).getCanonicalPath())) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN)
                    .body("Access denied.".getBytes());
        }

        // Error Handling and File Retrieval
        if (!file.exists() || !file.isFile()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body("File not found.".getBytes());
        }

        try (InputStream inputStream = new FileInputStream(file)) {
            byte[] fileContents = Files.readAllBytes(file.toPath());
            return ResponseEntity.ok()
                    .header("Content-Type", "image/jpeg") // Adjust the content type as needed
                    .body(fileContents);
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("An error occurred while reading the file.".getBytes());
        }
    }
}
