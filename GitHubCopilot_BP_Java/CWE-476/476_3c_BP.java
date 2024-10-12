package GitHubCopilot_BP_Java.CWE-476;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        // Memory Allocation
        byte[] buffer = new byte[1024];

        // Input Handling
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8))) {
            System.out.print("Enter up to 10 characters: ");
            String input = reader.readLine();

            // Input Validation
            if (input == null || input.length() > 10) {
                throw new IllegalArgumentException("Input must be 10 characters or less.");
            }

            // Data Encoding
            byte[] inputBytes = input.getBytes(StandardCharsets.UTF_8);

            // Buffer Size Limit
            if (inputBytes.length > buffer.length) {
                throw new ArrayIndexOutOfBoundsException("Input exceeds buffer size.");
            }

            // Copy input to buffer
            System.arraycopy(inputBytes, 0, buffer, 0, inputBytes.length);

            // Null Termination
            if (inputBytes.length < buffer.length) {
                buffer[inputBytes.length] = 0;
            }

            // Output the buffer content
            System.out.println("Buffer content: " + new String(buffer, 0, inputBytes.length, StandardCharsets.UTF_8));
        } catch (IOException e) {
            // Error Handling
            System.err.println("Error reading input: " + e.getMessage());
        } catch (IllegalArgumentException | ArrayIndexOutOfBoundsException e) {
            // Exception Handling
            System.err.println("Error: " + e.getMessage());
        } finally {
            // Memory Deallocation (not needed in Java, but for completeness)
            buffer = null;
        }
    }
}