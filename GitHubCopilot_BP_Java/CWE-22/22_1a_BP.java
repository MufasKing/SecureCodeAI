import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    private static final String SAFE_DIRECTORY = "/safe/";

    public static void main(String[] args) {
        String fileName = "example.txt"; // Example file name, replace with actual input
        try {
            readFile(fileName);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static void readFile(String fileName) throws IOException {
        validateFileName(fileName);
        File file = new File(SAFE_DIRECTORY, fileName);
        validateFilePath(file);

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        }
    }

    private static void validateFileName(String fileName) {
        if (fileName == null || fileName.isEmpty()) {
            throw new IllegalArgumentException("File name cannot be null or empty");
        }
        if (fileName.contains("..")) {
            throw new IllegalArgumentException("File name cannot contain path traversal characters");
        }
    }

    private static void validateFilePath(File file) throws IOException {
        String canonicalPath = file.getCanonicalPath();
        String safeCanonicalPath = new File(SAFE_DIRECTORY).getCanonicalPath();
        if (!canonicalPath.startsWith(safeCanonicalPath)) {
            throw new SecurityException("Access to the file is restricted to the safe directory");
        }
    }
}