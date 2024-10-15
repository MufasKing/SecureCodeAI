package GitHubCopilot_BP_Java.CWE_22;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Enumeration;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.zip.GZIPInputStream;
import org.apache.commons.compress.archivers.tar.TarArchiveEntry;
import org.apache.commons.compress.archivers.tar.TarArchiveInputStream;

public class Main {
    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length != 2) {
            LOGGER.severe("Usage: java Main <tar-file-path> <output-directory>");
            return;
        }

        String tarFilePath = args[0];
        String outputDirPath = args[1];

        try {
            validateAndExtractTarFile(tarFilePath, outputDirPath);
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "An error occurred while extracting the tar file", e);
        }
    }

    private static void validateAndExtractTarFile(String tarFilePath, String outputDirPath) throws IOException {
        Path tarPath = Paths.get(tarFilePath);
        Path outputPath = Paths.get(outputDirPath);

        // Validate input paths
        if (!Files.exists(tarPath) || !Files.isRegularFile(tarPath)) {
            throw new IllegalArgumentException("Invalid tar file path");
        }
        if (!Files.exists(outputPath) || !Files.isDirectory(outputPath)) {
            throw new IllegalArgumentException("Invalid output directory path");
        }

        // Open and extract tar file
        try (FileInputStream fis = new FileInputStream(tarPath.toFile());
             GZIPInputStream gis = new GZIPInputStream(fis);
             TarArchiveInputStream tis = new TarArchiveInputStream(gis)) {

            TarArchiveEntry entry;
            while ((entry = (TarArchiveEntry) tis.getNextEntry()) != null) {
                Path entryPath = outputPath.resolve(entry.getName()).normalize();

                // Prevent directory traversal attacks
                if (!entryPath.startsWith(outputPath)) {
                    throw new IOException("Entry is outside of the target dir: " + entry.getName());
                }

                if (entry.isDirectory()) {
                    Files.createDirectories(entryPath);
                } else {
                    Files.createDirectories(entryPath.getParent());
                    Files.copy(tis, entryPath);
                }
            }
        }
    }
}