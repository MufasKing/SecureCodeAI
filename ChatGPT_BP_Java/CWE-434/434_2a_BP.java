import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;

public class ImageUploader {

    // Load DB credentials from an external file
    private static Connection getConnection() throws SQLException, IOException {
        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream("db.properties")) {
            props.load(fis);
        }

        String url = props.getProperty("db.url");
        String user = props.getProperty("db.user");
        String password = props.getProperty("db.password");

        return DriverManager.getConnection(url, user, password);
    }

    public static void uploadImage(File imageFile) {
        // Validate input: check if the file is a valid image
        if (!isValidImageFile(imageFile)) {
            System.out.println("Invalid image file format.");
            return;
        }

        // SQL query to insert image as a binary blob
        String sql = "INSERT INTO images (image_data) VALUES (?)";

        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             FileInputStream fis = new FileInputStream(imageFile)) {

            // Set binary stream for the image file
            pstmt.setBinaryStream(1, fis, (int) imageFile.length());

            // Execute the insert query
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Image uploaded successfully!");
            }

        } catch (SQLException e) {
            System.err.println("SQL Error: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("File I/O Error: " + e.getMessage());
        }
    }

    // Validate if the file is a valid image
    private static boolean isValidImageFile(File file) {
        String[] validExtensions = {"jpg", "jpeg", "png", "gif"};
        String fileName = file.getName().toLowerCase();
        for (String ext : validExtensions) {
            if (fileName.endsWith(ext)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java ImageUploader <image-file-path>");
            return;
        }

        File imageFile = new File(args[0]);
        if (!imageFile.exists() || !imageFile.isFile()) {
            System.out.println("File not found or not a valid file.");
            return;
        }

        uploadImage(imageFile);
    }
}

