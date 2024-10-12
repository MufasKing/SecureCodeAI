import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.SecureRandom;
import java.util.Base64;

public class SecureRandomFloatToFile {
    public static void main(String[] args) {
        try {
            // Generate 3 random floats
            float[] randomFloats = generateSecureRandomFloats(3);

            // Convert them to strings
            String[] floatStrings = convertFloatsToStrings(randomFloats);

            // Concatenate them into a single string
            String concatenatedString = concatenateStrings(floatStrings);

            // Generate a secure filename
            String secureFileName = generateSecureFileName("output");

            // Write the concatenated string to a file
            writeStringToFile(concatenatedString, secureFileName);
            System.out.println("Data written to file: " + secureFileName);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static float[] generateSecureRandomFloats(int count) {
        SecureRandom secureRandom = new SecureRandom();
        float[] randomFloats = new float[count];

        for (int i = 0; i < count; i++) {
            randomFloats[i] = secureRandom.nextFloat();
        }
        return randomFloats;
    }

    private static String[] convertFloatsToStrings(float[] floats) {
        String[] floatStrings = new String[floats.length];

        for (int i = 0; i < floats.length; i++) {
            floatStrings[i] = Float.toString(floats[i]);
        }
        return floatStrings;
    }

    private static String concatenateStrings(String[] strings) {
        StringBuilder concatenatedString = new StringBuilder();

        for (String str : strings) {
            concatenatedString.append(str).append(" "); // Append with space for readability
        }
        return concatenatedString.toString().trim();
    }

    private static String generateSecureFileName(String baseName) {
        // Generate a secure random suffix
        SecureRandom secureRandom = new SecureRandom();
        byte[] randomBytes = new byte[8]; // 8 bytes = 64 bits
        secureRandom.nextBytes(randomBytes);
        String suffix = Base64.getUrlEncoder().withoutPadding().encodeToString(randomBytes);

        // Return a secure file name
        return baseName + "_" + suffix + ".txt";
    }

    private static void writeStringToFile(String data, String fileName) {
        Path filePath = Paths.get(fileName);

        // Create the file and write data securely
        try (BufferedWriter writer = Files.newBufferedWriter(filePath)) {
            writer.write(data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

