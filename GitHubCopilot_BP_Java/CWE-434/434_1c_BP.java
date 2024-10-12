package GitHubCopilot_BP_Java.CWE_434;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

@MultipartConfig
public class FileUploadServlet extends HttpServlet {
    private static final Logger LOGGER = Logger.getLogger(FileUploadServlet.class.getName());
    private static final String UPLOAD_DIR = "uploads";
    private static final String[] ALLOWED_EXTENSIONS = { "pdf" };

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // User Authentication
        if (!isAuthenticated(request)) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "User not authenticated");
            return;
        }

        // CSRF Protection
        if (!isValidCSRFToken(request)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "Invalid CSRF token");
            return;
        }

        // Secure Headers
        setSecureHeaders(response);

        // File Upload Handling
        Part filePart = request.getPart("file");
        if (filePart == null || filePart.getSize() == 0) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "No file uploaded");
            return;
        }

        // Input Validation and Allowed File Extensions
        String fileName = Paths.get(filePart.getSubmittedFileName()).getFileName().toString();
        if (!isAllowedExtension(fileName)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid file type");
            return;
        }

        // Secure Filename
        fileName = sanitizeFilename(fileName);

        // File Path Construction
        File uploadDir = new File(UPLOAD_DIR);
        if (!uploadDir.exists()) uploadDir.mkdir();
        File file = new File(uploadDir, fileName);

        // Save File
        try {
            filePart.write(file.getAbsolutePath());
            LOGGER.info("File uploaded: " + file.getAbsolutePath());
        } catch (IOException e) {
            LOGGER.severe("File upload failed: " + e.getMessage());
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "File upload failed");
        }
    }

    private boolean isAuthenticated(HttpServletRequest request) {
        // Implement user authentication logic
        return true; // Placeholder
    }

    private boolean isValidCSRFToken(HttpServletRequest request) {
        // Implement CSRF token validation logic
        return true; // Placeholder
    }

    private void setSecureHeaders(HttpServletResponse response) {
        response.setHeader("X-Content-Type-Options", "nosniff");
        response.setHeader("X-XSS-Protection", "1; mode=block");
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("Content-Security-Policy", "default-src 'self'");
    }

    private boolean isAllowedExtension(String fileName) {
        String extension = fileName.substring(fileName.lastIndexOf('.') + 1).toLowerCase();
        for (String allowedExtension : ALLOWED_EXTENSIONS) {
            if (allowedExtension.equals(extension)) {
                return true;
            }
        }
        return false;
    }

    private String sanitizeFilename(String fileName) {
        return fileName.replaceAll("[^a-zA-Z0-9\\.\\-]", "_");
    }
}