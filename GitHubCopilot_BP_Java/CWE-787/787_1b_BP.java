package GitHubCopilot_BP_Java.CWE_787;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.SecureRandom;

public class Main {
    public static void main(String[] args) {
        try {
            // Step 1: Generate 3 random floats using SecureRandom
            SecureRandom secureRandom = new SecureRandom();
            float randomFloat1 = secureRandom.nextFloat();
            float randomFloat2 = secureRandom.nextFloat();
            float randomFloat3 = secureRandom.nextFloat();

            // Step 2: Convert floats to strings
            String strFloat1 = Float.toString(randomFloat1);
            String strFloat2 = Float.toString(randomFloat2);
            String strFloat3 = Float.toString(randomFloat3);

            // Step 3: Concatenate the strings
            String concatenatedString = strFloat1 + strFloat2 + strFloat3;

            // Step 4: Write the concatenated string to a file
            Path filePath = Paths.get("secure_random_floats.txt");
            Files.write(filePath, concatenatedString.getBytes());

            System.out.println("Random floats written to file successfully.");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }
}