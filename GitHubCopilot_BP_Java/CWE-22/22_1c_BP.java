package GitHubCopilot_BP_Java.CWE_22;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    private static final String SAFE_DIRECTORY = "/path/to/safe/directory";

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Main <filename>");
            System.exit(1);
        }

        String requestedFile = args[0];
        try {
            String content = readFileFromSafeDirectory(requestedFile);
            System.out.println(content);
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    private static String readFileFromSafeDirectory(String filename) throws IOException {
        File safeDir = new File(SAFE_DIRECTORY);
        File file = new File(safeDir, filename).getCanonicalFile();

        // Ensure the file is within the safe directory
        if (!file.getPath().startsWith(safeDir.getCanonicalPath())) {
            throw new SecurityException("Attempt to access a file outside the safe directory");
        }

        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append(System.lineSeparator());
            }
        }
        return content.toString();
    }
}