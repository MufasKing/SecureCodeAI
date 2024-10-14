import java.io.*;
import java.nio.file.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class ZipExtractor {

    private static final String OUTPUT_DIR = "/tmp/unpack/";

    public static void main(String[] args) {
        String zipFilePath = "archive.zip";

        // Validate input
        if (!isValidZipFile(zipFilePath)) {
            System.err.println("Invalid ZIP file: " + zipFilePath);
            return;
        }

        try {
            extractZipFile(zipFilePath, OUTPUT_DIR);
            System.out.println("Extraction completed successfully!");
        } catch (IOException e) {
            System.err.println("Error during extraction: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static boolean isValidZipFile(String filePath) {
        // Basic validation for ZIP file extension
        return filePath != null && filePath.toLowerCase().endsWith(".zip");
    }

    private static void extractZipFile(String zipFilePath, String outputDir) throws IOException {
        File dir = new File(outputDir);
        if (!dir.exists()) {
            // Create the output directory if it doesn't exist
            if (!dir.mkdirs()) {
                throw new IOException("Failed to create output directory: " + outputDir);
            }
        }

        try (ZipInputStream zipInputStream = new ZipInputStream(new FileInputStream(zipFilePath))) {
            ZipEntry entry;
            while ((entry = zipInputStream.getNextEntry()) != null) {
                // Get the name of the entry
                String fileName = entry.getName();

                // Prevent directory traversal attacks
                if (fileName.contains("..")) {
                    throw new IOException("Invalid file path in ZIP entry: " + fileName);
                }

                // Create a new file output stream
                File newFile = new File(dir, fileName);
                if (entry.isDirectory()) {
                    // Create directory
                    if (!newFile.mkdirs()) {
                        throw new IOException("Failed to create directory: " + newFile.getAbsolutePath());
                    }
                } else {
                    // Create parent directories if necessary
                    new File(newFile.getParent()).mkdirs();

                    // Write the file contents
                    try (BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(newFile))) {
                        byte[] buffer = new byte[1024];
                        int bytesRead;
                        while ((bytesRead = zipInputStream.read(buffer)) != -1) {
                            bos.write(buffer, 0, bytesRead);
                        }
                    }
                }
                zipInputStream.closeEntry();
            }
        }
    }
}
