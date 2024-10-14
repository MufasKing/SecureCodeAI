import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class ZipExtractor {

    public static void main(String[] args) {
        String zipFilePath = "archive.zip"; // Path to the ZIP file
        Path tempDir = null;

        try {
            // Create a temporary directory
            tempDir = Files.createTempDirectory("unpack_");

            // Extract ZIP file to temporary directory
            extractZipFile(zipFilePath, tempDir);

            // Perform file validation (check if files are extracted)
            validateExtractedFiles(tempDir);

        } catch (IOException e) {
            System.err.println("Error during extraction: " + e.getMessage());
        } finally {
            // Cleanup: delete temporary directory
            if (tempDir != null) {
                try {
                    deleteDirectory(tempDir);
                } catch (IOException e) {
                    System.err.println("Failed to delete temporary directory: " + e.getMessage());
                }
            }
        }
    }

    private static void extractZipFile(String zipFilePath, Path destDir) throws IOException {
        try (InputStream fis = new FileInputStream(zipFilePath);
             ZipInputStream zis = new ZipInputStream(fis)) {
            ZipEntry entry;
            while ((entry = zis.getNextEntry()) != null) {
                File newFile = new File(destDir.toFile(), entry.getName());

                // Create directories for sub-directories in ZIP
                if (entry.isDirectory()) {
                    newFile.mkdirs();
                } else {
                    // Create all parent directories
                    new File(newFile.getParent()).mkdirs();

                    // Copy the ZIP entry to the new file
                    Files.copy(zis, newFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                }
                zis.closeEntry();
            }
        }
    }

    private static void validateExtractedFiles(Path dir) throws IOException {
        if (!Files.exists(dir) || !Files.isDirectory(dir)) {
            throw new IOException("No files extracted, directory does not exist: " + dir);
        }

        // List files in the directory (could perform additional checks)
        Files.list(dir).forEach(file -> {
            System.out.println("Extracted file: " + file.getFileName());
        });
    }

    private static void deleteDirectory(Path dir) throws IOException {
        Files.walk(dir)
                .sorted((a, b) -> b.compareTo(a)) // Sort in reverse order to delete files before directories
                .forEach(path -> {
                    try {
                        Files.delete(path);
                    } catch (IOException e) {
                        System.err.println("Failed to delete file: " + path + " - " + e.getMessage());
                    }
                });
    }
}
