import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MemoryAllocationExample {
    private static final int BUFFER_SIZE = 1024; // Size of the buffer

    public static void main(String[] args) {
        // Allocate first buffer
        char[] buf = allocateBuffer();
        // Read input into the first buffer
        readInput(buf, "Enter first 100 characters: ");

        // Allocate second buffer
        char[] buf1 = allocateBuffer();
        // Read input into the second buffer
        readInput(buf1, "Enter second 100 characters: ");

        // Clean up allocated memory (for demonstration purposes)
        cleanup(buf);
        cleanup(buf1);
    }

    // Method to allocate a buffer of specified size
    private static char[] allocateBuffer() {
        char[] buffer = new char[BUFFER_SIZE];
        System.out.println("Allocated buffer of size: " + BUFFER_SIZE);
        return buffer;
    }

    // Method to read input from stdin
    private static void readInput(char[] buffer, String prompt) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(prompt);
        
        try {
            String input = reader.readLine();
            // Input validation
            if (input.length() > 100) {
                System.out.println("Input exceeds 100 characters. Trimming to 100 characters.");
                input = input.substring(0, 100);
            }
            // Copy input to the buffer
            System.arraycopy(input.toCharArray(), 0, buffer, 0, input.length());
            System.out.println("Input read successfully.");
        } catch (IOException e) {
            System.err.println("Error reading input: " + e.getMessage());
        }
    }

    // Method to simulate cleanup
    private static void cleanup(char[] buffer) {
        // In Java, we rely on garbage collection, but we can nullify references
        buffer = null;
        System.out.println("Buffer cleaned up.");
    }
}
