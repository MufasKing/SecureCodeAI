import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MemoryAllocationExample {

    public static void main(String[] args) {
        // Memory allocation (simulated using an array)
        final int BUFFER_SIZE = 1024; // Allocating a buffer of 1024 bytes
        char[] buffer = new char[BUFFER_SIZE];

        try {
            // Input handling
            System.out.print("Enter up to 10 characters: ");
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = reader.readLine();

            // Input validation and buffer size limit
            if (input == null) {
                throw new IllegalArgumentException("Input cannot be null.");
            }
            if (input.length() > 10) {
                System.out.println("Input exceeds 10 characters, truncating...");
                input = input.substring(0, 10); // Truncate to 10 characters
            }

            // Copying data to buffer with null termination
            for (int i = 0; i < input.length(); i++) {
                buffer[i] = input.charAt(i);
            }
            buffer[input.length()] = '\0'; // Null terminate

            // Data encoding example (UTF-8 encoding)
            byte[] encodedData = new String(buffer, 0, input.length()).getBytes("UTF-8");
            System.out.println("Encoded data (in bytes):");
            for (byte b : encodedData) {
                System.out.print(b + " ");
            }
            System.out.println();

        } catch (IOException e) {
            // Exception handling for input/output errors
            System.err.println("An error occurred while reading input: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            // Exception handling for illegal arguments
            System.err.println("Input validation error: " + e.getMessage());
        } catch (Exception e) {
            // General exception handling
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            // Memory deallocation (simulated by setting the reference to null)
            buffer = null;
            System.out.println("Memory deallocated.");
        }
    }
}
