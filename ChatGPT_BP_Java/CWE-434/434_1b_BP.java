import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.MultipartConfig;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.Part;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.nio.file.attribute.PosixFilePermission;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.Set;

@WebServlet("/upload")
@MultipartConfig(fileSizeThreshold = 1024 * 1024, // 1MB threshold before saving to disk
                 maxFileSize = 10 * 1024 * 1024,  // Max 10MB file size
                 maxRequestSize = 50 * 1024 * 1024) // Max 50MB request size
public class UploadServlet extends HttpServlet {

    private static final String UPLOAD_DIR = "uploads";
    private static final String ALLOWED_FILE_TYPE = "application/pdf";

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Ensure folder exists and create with secure permissions if it doesn't
        File uploadDir = new File(UPLOAD_DIR);
        if (!uploadDir.exists()) {
            Set<PosixFilePermission> perms = PosixFilePermissions.fromString("rwxr-x---");
            Files.createDirectories(uploadDir.toPath(), PosixFilePermissions.asFileAttribute(perms));
        }

        // Get the uploaded file part from the form
        Part filePart = request.getPart("file");

        // Input Validation: Check if a file was selected
        if (filePart == null || filePart.getSize() == 0) {
            response.getWriter().println("No file uploaded or file is empty.");
            return;
        }

        // Check if it's a PDF file by content type
        if (!ALLOWED_FILE_TYPE.equals(filePart.getContentType())) {
            response.getWriter().println("Only PDF files are allowed.");
            return;
        }

        // Get filename and sanitize it
        String fileName = Paths.get(filePart.getSubmittedFileName()).getFileName().toString();
        fileName = sanitizeFileName(fileName);

        // Prevent path traversal attack
        if (fileName.contains("..")) {
            response.getWriter().println("Invalid file path.");
            return;
        }

        // Save the file in the "uploads" folder
        File file = new File(uploadDir, fileName);
        try (InputStream fileContent = filePart.getInputStream();
             FileOutputStream out = new FileOutputStream(file)) {
            filePart.write(file.getAbsolutePath());
            Files.copy(fileContent, file.toPath(), StandardCopyOption.REPLACE_EXISTING);

            // Set secure file permissions
            Set<PosixFilePermission> filePerms = PosixFilePermissions.fromString("rw-------");
            Files.setPosixFilePermissions(file.toPath(), filePerms);
        } catch (IOException e) {
            response.getWriter().println("File upload failed due to an error: " + e.getMessage());
            return;
        }

        response.getWriter().println("File uploaded successfully.");
    }

    private String sanitizeFileName(String fileName) {
        return fileName.replaceAll("[^a-zA-Z0-9\\.\\-]", "_");
    }
}
