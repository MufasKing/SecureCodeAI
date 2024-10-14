import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderExample {
    
    private static final String SAFE_DIRECTORY = "/safe/";
    
    public static void main(String[] args) {
        String fileName = "example.txt"; // Example file name; replace with actual file name
        readFile(fileName);
    }

    public static void readFile(String fileName) {
        // Input Validation
        if (!isValidFileName(fileName)) {
            System.err.println("Invalid file name provided.");
            return;
        }

        // Construct the file path
        File file = new File(SAFE_DIRECTORY + fileName);

        // Directory Restriction
        if (!isFileInSafeDirectory(file)) {
            System.err.println("Access denied. File must be in the safe directory.");
            return;
        }

        // Resource Cleanup and Error Handling
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
    }

    // Method to validate the file name
    private static boolean isValidFileName(String fileName) {
        // Simple validation to avoid special characters
        return fileName != null && !fileName.trim().isEmpty() && !fileName.contains("..") && fileName.matches("[a-zA-Z0-9_.]+");
    }

    // Method to check if the file is in the safe directory
    private static boolean isFileInSafeDirectory(File file) {
        return file.getAbsolutePath().startsWith(new File(SAFE_DIRECTORY).getAbsolutePath());
    }
}
