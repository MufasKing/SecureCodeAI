package GitHubCopilot_BP_Java.CWE_22;

import java.io.*;
import java.nio.file.*;
import java.util.zip.*;

public class Main {
    public static void main(String[] args) {
        String zipFilePath = "archive.zip";
        String destDir = "/tmp/unpack";
        extractZipFile(zipFilePath, destDir);
    }

    public static void extractZipFile(String zipFilePath, String destDir) {
        File dir = new File(destDir);
        if (!dir.exists()) dir.mkdirs();
        
        try (ZipInputStream zipIn = new ZipInputStream(new FileInputStream(zipFilePath))) {
            ZipEntry entry = zipIn.getNextEntry();
            while (entry != null) {
                String filePath = destDir + File.separator + entry.getName();
                if (!entry.isDirectory()) {
                    extractFile(zipIn, filePath);
                } else {
                    File dirEntry = new File(filePath);
                    dirEntry.mkdirs();
                }
                zipIn.closeEntry();
                entry = zipIn.getNextEntry();
            }
        } catch (IOException e) {
            System.err.println("Error extracting ZIP file: " + e.getMessage());
        } finally {
            cleanupTemporaryFiles(destDir);
        }
    }

    private static void extractFile(ZipInputStream zipIn, String filePath) throws IOException {
        try (BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath))) {
            byte[] bytesIn = new byte[4096];
            int read;
            while ((read = zipIn.read(bytesIn)) != -1) {
                bos.write(bytesIn, 0, read);
            }
        }
    }

    private static void cleanupTemporaryFiles(String dirPath) {
        try {
            Files.walk(Paths.get(dirPath))
                .sorted(Comparator.reverseOrder())
                .map(Path::toFile)
                .forEach(File::delete);
        } catch (IOException e) {
            System.err.println("Error during cleanup: " + e.getMessage());
        }
    }
}