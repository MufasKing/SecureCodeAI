package com.example.fileupload;

import org.apache.commons.io.FilenameUtils;
import org.apache.commons.io.IOUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.server.ResponseStatusException;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.SecureRandom;
import java.time.LocalDateTime;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Pattern;

@SpringBootApplication
public class FileUploadApplication {

    public static void main(String[] args) {
        SpringApplication.run(FileUploadApplication.class, args);
    }
}

@Controller
class FileUploadController {

    private static final Logger logger = LoggerFactory.getLogger(FileUploadController.class);

    private static final long MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
    private static final List<String> ALLOWED_EXTENSIONS = List.of("png", "jpg", "jpeg", "pdf", "txt");
    private static final Pattern FILENAME_SANITIZATION_PATTERN = Pattern.compile("[^a-zA-Z0-9._-]");
    private static final Path UPLOAD_DIR = Paths.get("uploads");
    private static final int MAX_REQUESTS_PER_MINUTE = 10;
    private static final AtomicInteger REQUEST_COUNT = new AtomicInteger(0);
    private static LocalDateTime lastRequestTime = LocalDateTime.now();

    // Ensure the upload directory exists
    static {
        try {
            if (!Files.exists(UPLOAD_DIR)) {
                Files.createDirectories(UPLOAD_DIR);
            }
        } catch (IOException e) {
            throw new RuntimeException("Could not initialize upload directory", e);
        }
    }

    @RequestMapping("/")
    public String index(Model model) {
        return "index"; // Reference a Thymeleaf template (index.html) for the form
    }

    @PostMapping("/upload")
    public ResponseEntity<String> handleFileUpload(@RequestParam("file") MultipartFile file) {
        // Rate limiting: Allow only a certain number of requests per minute
        if (isRateLimited()) {
            logger.warn("Too many requests. Rate limiting in effect.");
            return ResponseEntity.status(HttpStatus.TOO_MANY_REQUESTS).body("Rate limit exceeded. Try again later.");
        }

        // Validate file size
        if (file.getSize() > MAX_FILE_SIZE) {
            logger.warn("File too large: {} bytes", file.getSize());
            return ResponseEntity.status(HttpStatus.PAYLOAD_TOO_LARGE).body("File size exceeds limit (5MB)");
        }

        // Validate file extension
        String originalFilename = StringUtils.cleanPath(file.getOriginalFilename());
        String extension = FilenameUtils.getExtension(originalFilename).toLowerCase();
        if (!ALLOWED_EXTENSIONS.contains(extension)) {
            logger.warn("Invalid file extension: {}", extension);
            return ResponseEntity.status(HttpStatus.UNSUPPORTED_MEDIA_TYPE).body("Invalid file extension");
        }

        // Sanitize file name
        String sanitizedFilename = sanitizeFilename(originalFilename);

        // Save the file securely
        try {
            saveFileSecurely(file.getInputStream(), sanitizedFilename);
            logger.info("File uploaded successfully: {}", sanitizedFilename);
            return ResponseEntity.ok("File uploaded successfully: " + sanitizedFilename);
        } catch (IOException e) {
            logger.error("Error while saving file: {}", e.getMessage());
            throw new ResponseStatusException(HttpStatus.INTERNAL_SERVER_ERROR, "Error saving file");
        }
    }

    // Filename sanitization to prevent malicious filenames
    private String sanitizeFilename(String filename) {
        String baseName = FilenameUtils.getBaseName(filename);
        String extension = FilenameUtils.getExtension(filename);
        String sanitizedBaseName = FILENAME_SANITIZATION_PATTERN.matcher(baseName).replaceAll("_");
        return sanitizedBaseName + "." + extension;
    }

    // Securely save the file with a random prefix to avoid overwriting
    private void saveFileSecurely(InputStream inputStream, String filename) throws IOException {
        SecureRandom random = new SecureRandom();
        String randomPrefix = String.format("%016x", random.nextLong());
        Path filePath = UPLOAD_DIR.resolve(randomPrefix + "_" + filename);

        try (FileOutputStream fos = new FileOutputStream(filePath.toFile())) {
            IOUtils.copy(inputStream, fos);
        }
    }

    // Rate limiting logic: Allow only a certain number of requests per minute
    private boolean isRateLimited() {
        LocalDateTime now = LocalDateTime.now();
        if (now.isAfter(lastRequestTime.plusMinutes(1))) {
            REQUEST_COUNT.set(0);
            lastRequestTime = now;
        }

        return REQUEST_COUNT.incrementAndGet() > MAX_REQUESTS_PER_MINUTE;
    }

    // Error handling for various exceptions
    @ExceptionHandler(ResponseStatusException.class)
    public ResponseEntity<String> handleResponseStatusException(ResponseStatusException e) {
        logger.error("ResponseStatusException: {}", e.getMessage());
        return ResponseEntity.status(e.getStatus()).body(e.getReason());
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleGenericException(Exception e) {
        logger.error("Exception: {}", e.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("An unexpected error occurred");
    }
}
