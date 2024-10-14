import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class SecureFileReader {

    // Define the safe directory where files can be read from
    private static final String SAFE_DIRECTORY = "/path/to/safe/directory";

    public static void main(String[] args) {
        String fileName = "example.txt"; // Example file name
        readFile(fileName);
    }

    public static void readFile(String fileName) {
        // Validate the file name to prevent directory traversal attacks
        if (!isValidFileName(fileName)) {
            System.err.println("Invalid file name: " + fileName);
            return;
        }

        // Create a Path object for the file
        Path filePath = Paths.get(SAFE_DIRECTORY, fileName).normalize();

        // Check if the file is within the safe directory
        if (!filePath.startsWith(Paths.get(SAFE_DIRECTORY).normalize())) {
            System.err.println("Access denied to file: " + filePath);
            return;
        }

        File file = filePath.toFile();

        // Read the file securely with error handling
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + file.getAbsolutePath());
        } catch (IOException e) {
            System.err.println("Error reading file: " + file.getAbsolutePath());
            e.printStackTrace();
        }
    }

    // Validate the file name to prevent code injection and path traversal
    private static boolean isValidFileName(String fileName) {
        // Allow only alphanumeric characters, underscores, and dots
        return fileName.matches("^[a-zA-Z0-9._-]+$");
    }
}
