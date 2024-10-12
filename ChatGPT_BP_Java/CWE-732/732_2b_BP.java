import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class FileHandler {

    public static void main(String[] args) {
        String filePath = "example.txt"; // Specify your file path here
        openFile(filePath);
    }

    public static void openFile(String filePath) {
        Path path = Path.of(filePath);

        // Check if the file already exists
        if (Files.exists(path)) {
            System.out.println("File already exists. Truncating the file...");
        } else {
            System.out.println("File does not exist. Creating a new file...");
        }

        try {
            // Open file in write mode with specified options
            // O_CREAT, O_TRUNC, O_WRONLY, O_EXCL behavior:
            Files.writeString(path, "", StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING, StandardOpenOption.WRITE);

            // Example of writing data to the file
            String dataToWrite = "This is a test data.";
            Files.writeString(path, dataToWrite, StandardOpenOption.APPEND);

            System.out.println("File has been opened/created and data has been written successfully.");

        } catch (IOException e) {
            System.err.println("An error occurred while opening the file: " + e.getMessage());
        }
    }
}
