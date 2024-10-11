import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class FileChecksumCalculator {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: java FileChecksumCalculator <inputFile> <outputFile>");
            System.exit(1);
        }

        String inputFile = args[0];
        String outputFile = args[1];

        try {
            byte[] buffer = readFile(inputFile);
            long checksum = calculateChecksum(buffer);

            // Check if the buffer is empty
            if (checksum == 0) {
                System.out.println("The buffer is empty.");
            } else {
                System.out.printf("Checksum: %d, Bytes Read: %d%n", checksum, buffer.length);
            }

            writeOutput(outputFile, buffer.length, checksum);
        } catch (IOException | NoSuchAlgorithmException e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static byte[] readFile(String filePath) throws IOException {
        // Input validation
        if (filePath == null || filePath.isEmpty()) {
            throw new IllegalArgumentException("File path cannot be null or empty.");
        }

        // Read the file into a byte array
        return Files.readAllBytes(Paths.get(filePath));
    }

    private static long calculateChecksum(byte[] data) throws NoSuchAlgorithmException {
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null.");
        }

        // Using SHA-256 for checksum
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(data);
        
        // Convert byte array to long for easier readability
        return byteArrayToLong(hash);
    }

    private static long byteArrayToLong(byte[] byteArray) {
        long result = 0;
        for (int i = 0; i < Math.min(byteArray.length, Long.BYTES); i++) {
            result = (result << 8) | (byteArray[i] & 0xFF);
        }
        return result;
    }

    private static void writeOutput(String outputFile, long bytesRead, long checksum) throws IOException {
        // Ensure the output file path is valid
        if (outputFile == null || outputFile.isEmpty()) {
            throw new IllegalArgumentException("Output file path cannot be null or empty.");
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            writer.write("Bytes Read: " + bytesRead + "\n");
            writer.write("Checksum: " + checksum + "\n");
        }
    }
}
