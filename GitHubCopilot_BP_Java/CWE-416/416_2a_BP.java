import java.io.*;
import java.nio.file.*;
import java.security.*;
import java.util.Formatter;

public class Main {
    public static void main(String[] args) {
        String inputFilePath = "input.txt";
        String outputFilePath = "output.txt";

        if (inputFilePath == null || inputFilePath.isEmpty() || outputFilePath == null || outputFilePath.isEmpty()) {
            System.err.println("File paths must not be null or empty.");
            return;
        }

        try {
            byte[] buffer = Files.readAllBytes(Paths.get(inputFilePath));
            int bytesRead = buffer.length;

            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] checksumBytes = digest.digest(buffer);
            String checksum = bytesToHex(checksumBytes);

            if (checksum.equals(bytesToHex(digest.digest(new byte[0])))) {
                System.out.println("The buffer is empty.");
            }

            try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(outputFilePath))) {
                writer.write(String.format("Bytes read: %d%n", bytesRead));
                writer.write(String.format("Checksum: %s%n", checksum));
            }

        } catch (IOException | NoSuchAlgorithmException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    private static String bytesToHex(byte[] bytes) {
        try (Formatter formatter = new Formatter()) {
            for (byte b : bytes) {
                formatter.format("%02x", b);
            }
            return formatter.toString();
        }
    }
}