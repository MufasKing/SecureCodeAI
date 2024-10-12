package GitHubCopilot_BP_Java.CWE_434;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.List;

@SpringBootApplication
@EnableWebMvc
public class MainApplication implements WebMvcConfigurer {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**").allowedOrigins("*");
    }

    @Bean
    public FileUploadController fileUploadController() {
        return new FileUploadController();
    }
}

@RestController
@RequestMapping("/upload")
class FileUploadController {

    private static final String UPLOAD_DIR = "uploads/";
    private static final List<String> ALLOWED_EXTENSIONS = Arrays.asList("jpg", "png", "pdf", "txt");
    private static final long MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB

    @PostMapping
    public ResponseEntity<String> uploadFile(@RequestParam("file") MultipartFile file, HttpServletRequest request) {
        try {
            // CSRF Protection
            if (!isValidCsrfToken(request)) {
                return ResponseEntity.status(HttpStatus.FORBIDDEN).body("Invalid CSRF token");
            }

            // Input Validation
            if (file.isEmpty()) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("File is empty");
            }

            // File Size Validation
            if (file.getSize() > MAX_FILE_SIZE) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("File size exceeds limit");
            }

            // File Extension Validation
            String fileExtension = StringUtils.getFilenameExtension(file.getOriginalFilename());
            if (!ALLOWED_EXTENSIONS.contains(fileExtension)) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid file extension");
            }

            // File Type Validation
            if (!file_is_safe_type(file)) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid file type");
            }

            // Secure Filename
            String secureFilename = sanitizeFilename(file.getOriginalFilename());

            // Existing File Check
            Path filePath = Paths.get(UPLOAD_DIR, secureFilename);
            if (Files.exists(filePath)) {
                return ResponseEntity.status(HttpStatus.CONFLICT).body("File already exists");
            }

            // Secure File Writing
            Files.copy(file.getInputStream(), filePath);

            return ResponseEntity.ok("File uploaded successfully");
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("File upload failed");
        }
    }

    private boolean file_is_safe_type(MultipartFile file) {
        // Stub function, always returns true
        return true;
    }

    private boolean isValidCsrfToken(HttpServletRequest request) {
        // Implement CSRF token validation logic
        return true;
    }

    private String sanitizeFilename(String filename) {
        return filename.replaceAll("[^a-zA-Z0-9\\.\\-]", "_");
    }
}