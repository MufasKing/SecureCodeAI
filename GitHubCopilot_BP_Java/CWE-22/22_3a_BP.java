package GitHubCopilot_BP_Java.CWE-22;

import java.io.*;
import java.nio.file.*;
import java.util.zip.*;

public class Main {
    public static void main(String[] args) {
        String zipFilePath = "archive.zip";
        String destDir = "/tmp/unpack";
        
        try {
            unzip(zipFilePath, destDir);
        } catch (IOException e) {
            System.err.println("Error unzipping file: " + e.getMessage());
        }
    }

    public static void unzip(String zipFilePath, String destDir) throws IOException {
        File destDirFile = new File(destDir);
        if (!destDirFile.exists()) {
            destDirFile.mkdirs();
        }

        try (ZipInputStream zipIn = new ZipInputStream(new FileInputStream(zipFilePath))) {
            ZipEntry entry = zipIn.getNextEntry();
            while (entry != null) {
                String filePath = destDir + File.separator + entry.getName();
                if (!isValidPath(filePath, destDir)) {
                    throw new IOException("Invalid file path: " + filePath);
                }
                if (!entry.isDirectory()) {
                    extractFile(zipIn, filePath);
                } else {
                    File dir = new File(filePath);
                    dir.mkdirs();
                }
                zipIn.closeEntry();
                entry = zipIn.getNextEntry();
            }
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

    private static boolean isValidPath(String filePath, String destDir) throws IOException {
        Path destDirPath = Paths.get(destDir).toRealPath();
        Path filePathPath = Paths.get(filePath).toRealPath();
        return filePathPath.startsWith(destDirPath);
    }
}