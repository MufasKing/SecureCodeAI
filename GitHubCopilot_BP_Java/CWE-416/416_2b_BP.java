import java.io.*;
import java.security.*;

public class Main {
    public static void main(String[] args) {
        String inputFilePath = "input.txt";
        String outputFilePath = "output.txt";

        try {
            byte[] buffer = readFileToBuffer(inputFilePath);
            byte[] checksum = calculateChecksum(buffer);
            int bytesRead = buffer.length;

            writeResultsToFile(outputFilePath, bytesRead, checksum);
        } catch (IOException | NoSuchAlgorithmException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    private static byte[] readFileToBuffer(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists() || !file.isFile()) {
            throw new FileNotFoundException("File not found: " + filePath);
        }

        try (FileInputStream fis = new FileInputStream(file)) {
            byte[] buffer = new byte[(int) file.length()];
            int bytesRead = fis.read(buffer);
            if (bytesRead != buffer.length) {
                throw new IOException("Could not read the entire file");
            }
            return buffer;
        }
    }

    private static byte[] calculateChecksum(byte[] buffer) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        return digest.digest(buffer);
    }

    private static void writeResultsToFile(String filePath, int bytesRead, byte[] checksum) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filePath);
             DataOutputStream dos = new DataOutputStream(fos)) {
            dos.writeInt(bytesRead);
            dos.write(checksum);
        }
    }
}