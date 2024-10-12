package GitHubCopilot_BP_Java.CWE_434;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.util.StringUtils;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

@SpringBootApplication
@EnableWebMvc
@RestController
public class Main {

    private static final Logger logger = Logger.getLogger(Main.class.getName());
    private static final String UPLOAD_DIR = "uploads/";
    private static final long MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB
    private static final List<String> ALLOWED_EXTENSIONS = Arrays.asList("jpg", "png", "pdf", "txt");

    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @PostMapping("/upload")
    public ResponseEntity<String> handleFileUpload(@RequestParam("file") MultipartFile file) {
        // Check file size
        if (file.getSize() > MAX_FILE_SIZE) {
            return ResponseEntity.status(HttpStatus.PAYLOAD_TOO_LARGE).body("File size exceeds limit!");
        }

        // Check file extension
        String fileExtension = StringUtils.getFilenameExtension(file.getOriginalFilename());
        if (fileExtension == null || !ALLOWED_EXTENSIONS.contains(fileExtension.toLowerCase())) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid file extension!");
        }

        // Sanitize filename
        String sanitizedFilename = StringUtils.cleanPath(file.getOriginalFilename());
        if (sanitizedFilename.contains("..")) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid filename!");
        }

        // Secure file storage
        try {
            Path uploadPath = Paths.get(UPLOAD_DIR + sanitizedFilename);
            Files.createDirectories(uploadPath.getParent());
            file.transferTo(uploadPath.toFile());
        } catch (IOException e) {
            logger.severe("File upload failed: " + e.getMessage());
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("File upload failed!");
        }

        logger.info("File uploaded successfully: " + sanitizedFilename);
        return ResponseEntity.ok("File uploaded successfully!");
    }

    // Rate-limiting and monitoring can be implemented using additional libraries or services
}