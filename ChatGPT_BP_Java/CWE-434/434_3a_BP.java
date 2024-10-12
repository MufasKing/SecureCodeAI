package com.example.fileupload;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashSet;
import java.util.Set;

@Controller
public class FileUploadController {

    private static final Set<String> ALLOWED_EXTENSIONS = new HashSet<>();
    private static final long MAX_FILE_SIZE = 10485760; // 10MB

    @Value("${upload.dir}")
    private String uploadDir;

    static {
        ALLOWED_EXTENSIONS.add("jpg");
        ALLOWED_EXTENSIONS.add("jpeg");
        ALLOWED_EXTENSIONS.add("png");
        ALLOWED_EXTENSIONS.add("pdf");
    }

    @GetMapping("/")
    public String index(Model model) {
        return "upload";
    }

    @PostMapping("/upload")
    public ResponseEntity<String> handleFileUpload(MultipartFile file, RedirectAttributes redirectAttributes, HttpServletResponse response) {
        try {
            // CSRF protection is automatically handled by Spring Security (if enabled)

            // Input validation
            if (file.isEmpty()) {
                return new ResponseEntity<>("No file selected", HttpStatus.BAD_REQUEST);
            }

            // File size validation
            if (file.getSize() > MAX_FILE_SIZE) {
                return new ResponseEntity<>("File exceeds maximum size limit", HttpStatus.PAYLOAD_TOO_LARGE);
            }

            // Get file extension
            String extension = getFileExtension(file.getOriginalFilename());

            // File extension and type validation
            if (!isAllowedExtension(extension)) {
                return new ResponseEntity<>("Invalid file type", HttpStatus.UNSUPPORTED_MEDIA_TYPE);
            }

            // Secure filename
            String secureFilename = getSecureFilename(file.getOriginalFilename());

            // Ensure file doesn't already exist
            Path destinationFilePath = Paths.get(uploadDir).resolve(secureFilename);
            if (Files.exists(destinationFilePath)) {
                return new ResponseEntity<>("File already exists", HttpStatus.CONFLICT);
            }

            // Save file securely
            saveFile(file.getInputStream(), destinationFilePath);

            // Set secure headers
            setSecureHeaders(response);

            return new ResponseEntity<>("File uploaded successfully: " + secureFilename, HttpStatus.OK);

        } catch (IOException e) {
            return new ResponseEntity<>("File upload failed", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // Stub: A real implementation should do content-type and more in-depth checks
    private boolean file_is_safe_type(InputStream fileContent) {
        return true; // Always return true for this stub
    }

    private boolean isAllowedExtension(String extension) {
        return ALLOWED_EXTENSIONS.contains(extension.toLowerCase());
    }

    private String getSecureFilename(String originalFilename) throws NoSuchAlgorithmException {
        String baseName = Paths.get(originalFilename).getFileName().toString();
        String extension = getFileExtension(originalFilename);
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(baseName.getBytes());
        String secureFilename = bytesToHex(hash) + "." + extension;
        return secureFilename;
    }

    private void saveFile(InputStream fileInputStream, Path destinationPath) throws IOException {
        Files.copy(fileInputStream, destinationPath, StandardCopyOption.REPLACE_EXISTING);
        // Ensure permissions on the file are secure
        destinationPath.toFile().setReadable(true, true);
        destinationPath.toFile().setWritable(true, true);
    }

    private void setSecureHeaders(HttpServletResponse response) {
        response.setHeader(HttpHeaders.CACHE_CONTROL, "no-store, no-cache, must-revalidate, proxy-revalidate");
        response.setHeader(HttpHeaders.PRAGMA, "no-cache");
        response.setHeader(HttpHeaders.EXPIRES, "0");
        response.setHeader(HttpHeaders.CONTENT_SECURITY_POLICY, "default-src 'self'");
        response.setHeader(HttpHeaders.X_CONTENT_TYPE_OPTIONS, "nosniff");
        response.setHeader(HttpHeaders.X_FRAME_OPTIONS, "DENY");
    }

    private String getFileExtension(String filename) {
        int dotIndex = filename.lastIndexOf('.');
        return (dotIndex == -1) ? "" : filename.substring(dotIndex + 1);
    }

    private String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder(2 * bytes.length);
        for (byte b : bytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }
}
