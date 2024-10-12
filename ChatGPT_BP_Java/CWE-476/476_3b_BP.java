import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ScannerExample {

    public static void main(String[] args) {
        // Call the scan function
        String input = scan();
        System.out.println("You entered: " + input);
    }

    public static String scan() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder inputBuilder = new StringBuilder();
        int characterCount = 0;
        char[] buffer = new char[1024];

        try {
            System.out.print("Enter a string (max 1023 characters): ");
            // Read up to 1023 characters
            characterCount = reader.read(buffer, 0, 1023);

            // Check if the input is null or exceeds the buffer limit
            if (characterCount == -1) {
                System.err.println("Error: End of stream reached unexpectedly.");
                return null; // End of stream
            }

            // Convert char array to String and trim to remove new line
            String input = new String(buffer, 0, characterCount).trim();
            inputBuilder.append(input);

            // Handle newline character (not stored in buffer)
            if (characterCount > 0 && buffer[characterCount - 1] == '\n') {
                // Newline character handled (not stored in input)
            }

        } catch (IOException e) {
            System.err.println("Error reading input: " + e.getMessage());
            return null; // Indicate an error occurred
        } finally {
            try {
                // Flush the reader if necessary
                reader.close();
            } catch (IOException e) {
                System.err.println("Error closing the reader: " + e.getMessage());
            }
        }

        return inputBuilder.toString();
    }
}
