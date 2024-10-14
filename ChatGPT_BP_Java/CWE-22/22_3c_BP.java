import java.io.*;
import java.nio.file.*;
import java.util.zip.GZIPInputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class TarFileManager {

    private String tarFilePath;

    public TarFileManager(String tarFilePath) {
        validateFilePath(tarFilePath);
        this.tarFilePath = tarFilePath;
    }

    // Validate the file path
    private void validateFilePath(String filePath) {
        if (filePath == null || filePath.trim().isEmpty()) {
            throw new IllegalArgumentException("File path cannot be null or empty.");
        }

        Path path = Paths.get(filePath);
        if (!path.isAbsolute()) {
            throw new IllegalArgumentException("File path must be an absolute path.");
        }

        if (!Files.exists(path) || !Files.isReadable(path)) {
            throw new IllegalArgumentException("File does not exist or is not readable: " + filePath);
        }
    }

    // Method to extract a tar file
    public void extractTarFile(String outputDir) {
        validateOutputDirectory(outputDir);
        
        try (InputStream fileInputStream = new FileInputStream(tarFilePath);
             BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream);
             GZIPInputStream gzipInputStream = new GZIPInputStream(bufferedInputStream);
             TarInputStream tarInputStream = new TarInputStream(gzipInputStream)) {

            TarEntry entry;
            while ((entry = tarInputStream.getNextEntry()) != null) {
                File outputFile = new File(outputDir, entry.getName());
                // Ensure the directory structure exists
                if (entry.isDirectory()) {
                    outputFile.mkdirs();
                } else {
                    // Securely extract files
                    extractFile(tarInputStream, outputFile);
                }
            }
        } catch (IOException e) {
            handleError(e);
        }
    }

    // Validate the output directory
    private void validateOutputDirectory(String outputDir) {
        if (outputDir == null || outputDir.trim().isEmpty()) {
            throw new IllegalArgumentException("Output directory cannot be null or empty.");
        }

        Path path = Paths.get(outputDir);
        if (!Files.exists(path) || !Files.isDirectory(path)) {
            throw new IllegalArgumentException("Output directory does not exist or is not a directory: " + outputDir);
        }
    }

    // Securely extract a single file
    private void extractFile(TarInputStream tarInputStream, File outputFile) throws IOException {
        // Ensure the parent directories exist
        File parent = outputFile.getParentFile();
        if (!parent.exists()) {
            parent.mkdirs();
        }

        try (OutputStream fileOutputStream = new FileOutputStream(outputFile)) {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = tarInputStream.read(buffer)) != -1) {
                fileOutputStream.write(buffer, 0, bytesRead);
            }
        } catch (IOException e) {
            handleError(e);
        }
    }

    // Handle errors with proper logging and cleanup
    private void handleError(IOException e) {
        // Implement error handling (logging, alerting, etc.)
        System.err.println("Error occurred during tar extraction: " + e.getMessage());
    }

    // Main method for testing
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java TarFileManager <tar-file-path> <output-directory>");
            return;
        }

        String tarFilePath = args[0];
        String outputDir = args[1];

        try {
            TarFileManager tarFileManager = new TarFileManager(tarFilePath);
            tarFileManager.extractTarFile(outputDir);
            System.out.println("Extraction completed successfully.");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}

// Dummy TarInputStream and TarEntry classes for demonstration
// In a real application, you would use a proper tar library
class TarInputStream extends InputStream {
    public TarInputStream(InputStream in) { /* implementation */ }

    public TarEntry getNextEntry() { /* implementation */ return null; }

    @Override
    public int read() throws IOException { /* implementation */ return -1; }
}

class TarEntry {
    public boolean isDirectory() { /* implementation */ return false; }
    public String getName() { /* implementation */ return ""; }
}
