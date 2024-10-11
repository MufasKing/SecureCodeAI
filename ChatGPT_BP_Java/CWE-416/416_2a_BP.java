import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class FileChecksum {

    // Method to read file into a byte buffer
    public static byte[] readFileToBuffer(String filePath) throws IOException {
        // Validate input
        if (filePath == null || filePath.trim().isEmpty()) {
            throw new IllegalArgumentException("File path cannot be null or empty.");
        }

        return Files.readAllBytes(Paths.get(filePath));
    }

    // Method to calculate checksum using SHA-256
    public static String calculateChecksum(byte[] buffer) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(buffer);
        StringBuilder hexString = new StringBuilder();

        for (byte b : hash) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        return hexString.toString();
    }

    // Method to write output to a file
    public static void writeOutputToFile(String outputPath, int bytesRead, String checksum) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath))) {
            writer.write(String.format("Bytes Read: %d\n", bytesRead));
            writer.write(String.format("Checksum: %s\n", checksum));
        }
    }

    public static void main(String[] args) {
        // Input file path and output file path
        String inputFilePath = "input.txt";  // Specify your input file path
        String outputFilePath = "output.txt"; // Specify your output file path

        try {
            // Read the contents of the file into a buffer
            byte[] buffer = readFileToBuffer(inputFilePath);
            int bytesRead = buffer.length;

            // Calculate the checksum
            String checksum = calculateChecksum(buffer);

            // Check if the buffer is empty
            if (bytesRead == 0) {
                System.out.println("The buffer is empty.");
            } else {
                System.out.println("Checksum calculated successfully.");
            }

            // Write the number of bytes read and checksum to the output file
            writeOutputToFile(outputFilePath, bytesRead, checksum);
            System.out.println("Output written to file successfully.");

        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
        } catch (NoSuchAlgorithmException e) {
            System.err.println("Hashing algorithm error: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.err.println("Input validation error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
