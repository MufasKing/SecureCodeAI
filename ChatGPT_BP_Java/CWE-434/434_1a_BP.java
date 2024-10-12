import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

@MultipartConfig(fileSizeThreshold = 1024 * 1024, // 1MB
                 maxFileSize = 1024 * 1024 * 10,  // 10MB
                 maxRequestSize = 1024 * 1024 * 50) // 50MB
public class FileUploadServlet extends HttpServlet {

    private static final String UPLOAD_DIR = "uploads";
    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydatabase";
    private static final String DB_USER = "upload_user";  // Principle of least privilege
    private static final String DB_PASSWORD = "securepassword";

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {

        // Access control: Ensure user is authenticated
        if (!isAuthenticated(request)) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Unauthorized access.");
            return;
        }

        // Get file part from the request
        Part filePart = request.getPart("pdfFile");
        
        // Input validation: Check if the file is a PDF
        String fileName = getFileName(filePart);
        if (!fileName.endsWith(".pdf")) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid file type. Only PDFs are allowed.");
            return;
        }

        // File handling: Save the file to the uploads directory
        String uploadPath = getServletContext().getRealPath("") + File.separator + UPLOAD_DIR;
        File uploadDir = new File(uploadPath);
        if (!uploadDir.exists()) uploadDir.mkdir();

        String filePath = uploadPath + File.separator + fileName;
        try {
            filePart.write(filePath);
        } catch (IOException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Error while saving file.");
            return;
        }

        // Save the file path in the database
        try {
            saveFilePathToDatabase(filePath);
        } catch (SQLException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error.");
            return;
        }

        // Send success response
        response.getWriter().println("File uploaded and saved successfully.");
    }

    private boolean isAuthenticated(HttpServletRequest request) {
        // Implement your access control logic here (e.g., session checks)
        return request.getSession().getAttribute("user") != null;
    }

    private String getFileName(Part part) {
        String contentDisposition = part.getHeader("content-disposition");
        for (String cd : contentDisposition.split(";")) {
            if (cd.trim().startsWith("filename")) {
                return cd.substring(cd.indexOf('=') + 1).trim().replace("\"", "");
            }
        }
        return null;
    }

    private void saveFilePathToDatabase(String filePath) throws SQLException {
        // Parameterized Query to prevent SQL injection
        String sql = "INSERT INTO uploaded_files (file_path) VALUES (?)";
        
        // Use a try-with-resources block for automatic resource management
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, filePath);
            stmt.executeUpdate();
        }
    }
}
