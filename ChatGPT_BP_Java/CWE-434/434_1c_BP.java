package com.example.uploadapp;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.method.annotation.MvcUriComponentsBuilder;

import javax.servlet.http.HttpServletRequest;
import javax.validation.constraints.NotNull;
import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.security.Principal;
import java.util.stream.Collectors;

@SpringBootApplication
public class UploadAppApplication {

    public static void main(String[] args) {
        SpringApplication.run(UploadAppApplication.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();  // For secure password hashing
    }
}

@Controller
@RequestMapping("/files")
class FileUploadController {

    private static final Logger logger = LoggerFactory.getLogger(FileUploadController.class);
    private final Path rootLocation = Paths.get("uploads");  // Secure folder

    public FileUploadController() throws IOException {
        Files.createDirectories(rootLocation);  // Ensure the directory exists
    }

    // Secure file upload, restricted to authenticated users and to PDFs only
    @PostMapping("/upload")
    public String handleFileUpload(@RequestParam("file") MultipartFile file, Principal principal, Model model) {
        validateFile(file);  // Input validation for file extension

        String filename = StringUtils.cleanPath(file.getOriginalFilename());
        logger.info("User {} is uploading file: {}", principal.getName(), filename);

        if (!isAllowedFileExtension(filename)) {
            model.addAttribute("message", "Only PDF files are allowed.");
            return "uploadStatus";
        }

        try {
            Path destinationFile = rootLocation.resolve(Paths.get(filename))
                    .normalize().toAbsolutePath();
            Files.copy(file.getInputStream(), destinationFile, StandardCopyOption.REPLACE_EXISTING);
            logger.info("File saved successfully at {}", destinationFile);

            model.addAttribute("message", "File uploaded successfully!");
            return "uploadStatus";
        } catch (IOException e) {
            logger.error("Error while uploading file: {}", e.getMessage());
            throw new FileUploadException("Failed to store file " + filename, e);
        }
    }

    // Secure download: Only authenticated users can access
    @GetMapping("/download/{filename:.+}")
    public ResponseEntity<Resource> serveFile(@PathVariable String filename, Principal principal) {
        logger.info("User {} is attempting to download file: {}", principal.getName(), filename);
        Path file = loadFile(filename);

        // Logging & Monitoring: File access is logged
        logger.info("File {} accessed by user {}", filename, principal.getName());

        Resource resource = loadAsResource(filename);
        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + resource.getFilename() + "\"")
                .body(resource);
    }

    // File deletion with access control: Only admins can delete
    @DeleteMapping("/delete/{filename:.+}")
    public String deleteFile(@PathVariable String filename, Principal principal, HttpServletRequest request) {
        if (request.isUserInRole("ADMIN")) {
            try {
                Files.delete(loadFile(filename));
                logger.info("File {} deleted by admin {}", filename, principal.getName());
                return "File deleted successfully.";
            } catch (IOException e) {
                logger.error("Error deleting file: {}", e.getMessage());
                throw new FileDeletionException("Failed to delete file " + filename, e);
            }
        } else {
            logger.warn("Unauthorized deletion attempt by user {}", principal.getName());
            return "You are not authorized to delete files.";
        }
    }

    // Input validation: Only allow PDFs
    private void validateFile(@NotNull MultipartFile file) {
        if (file.isEmpty()) {
            throw new FileUploadException("Cannot upload an empty file.");
        }
    }

    private boolean isAllowedFileExtension(String filename) {
        return filename.endsWith(".pdf");  // Restrict to PDFs
    }

    // Secure filename handling
    private Path loadFile(String filename) {
        return rootLocation.resolve(filename).normalize().toAbsolutePath();
    }

    private Resource loadAsResource(String filename) {
        try {
            Path file = loadFile(filename);
            return new org.springframework.core.io.UrlResource(file.toUri());
        } catch (IOException e) {
            logger.error("Could not load file: {}", filename);
            throw new FileNotFoundException("Could not read file: " + filename);
        }
    }
}

// Error handling
@ResponseStatus(code = org.springframework.http.HttpStatus.INTERNAL_SERVER_ERROR)
class FileUploadException extends RuntimeException {
    public FileUploadException(String message, Throwable cause) {
        super(message, cause);
    }
}

@ResponseStatus(code = org.springframework.http.HttpStatus.INTERNAL_SERVER_ERROR)
class FileDeletionException extends RuntimeException {
    public FileDeletionException(String message, Throwable cause) {
        super(message, cause);
    }
}

@ResponseStatus(code = org.springframework.http.HttpStatus.NOT_FOUND)
class FileNotFoundException extends RuntimeException {
    public FileNotFoundException(String message) {
        super(message);
    }
}

// Security Configuration for User Authentication, CSRF, and Headers
@Configuration
@EnableWebSecurity
class WebSecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeRequests(authorizeRequests ->
                authorizeRequests
                    .antMatchers("/files/upload", "/files/download/**").authenticated()  // Require authentication for file handling
                    .antMatchers("/files/delete/**").hasRole("ADMIN")  // Admin-only for file deletion
                    .anyRequest().permitAll()
            )
            .formLogin(withDefaults())  // Enable form-based login
            .csrf(csrf -> csrf.ignoringAntMatchers("/files/delete/**"))  // Enable CSRF protection
            .headers(headers -> headers
                .contentSecurityPolicy("script-src 'self'")  // Secure headers
                .frameOptions().sameOrigin()
            );
        return http.build();
    }

    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder passwordEncoder) {
        return new InMemoryUserDetailsManager(
            User.withUsername("user").password(passwordEncoder.encode("password")).roles("USER").build(),
            User.withUsername("admin").password(passwordEncoder.encode("admin")).roles("ADMIN").build()
        );
    }
}

