package GitHubCopilot_BP_Java.CWE-434;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        String filePath = "path/to/image.jpg"; // Replace with actual file path
        if (isValidImage(filePath)) {
            try {
                storeImageInDatabase(filePath);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("Invalid image file.");
        }
    }

    private static boolean isValidImage(String filePath) {
        File file = new File(filePath);
        String mimeType = getMimeType(file);
        long fileSize = file.length();
        
        return mimeType.startsWith("image/") && fileSize <= 5 * 1024 * 1024; // 5MB limit
    }

    private static String getMimeType(File file) {
        // Implement a method to get the MIME type of the file
        // This can be done using libraries like Apache Tika
        return "image/jpeg"; // Placeholder
    }

    private static void storeImageInDatabase(String filePath) throws IOException, SQLException {
        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream("db.properties")) {
            props.load(fis);
        }

        String url = props.getProperty("db.url");
        String user = props.getProperty("db.user");
        String password = props.getProperty("db.password");

        try (Connection conn = DriverManager.getConnection(url, user, password);
             FileInputStream fis = new FileInputStream(filePath);
             PreparedStatement pstmt = conn.prepareStatement("INSERT INTO images (image) VALUES (?)")) {

            pstmt.setBinaryStream(1, fis, (int) new File(filePath).length());
            pstmt.executeUpdate();
            System.out.println("Image stored successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
            throw e;
        } catch (IOException e) {
            e.printStackTrace();
            throw e;
        }
    }
}