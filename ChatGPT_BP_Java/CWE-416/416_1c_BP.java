import java.security.SecureRandom;
import java.util.Scanner;

public class SecureBufferExample {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        SecureRandom secureRandom = new SecureRandom();
        int bufferSize = 0;

        // Input Validation
        while (true) {
            System.out.print("Enter a positive integer for buffer size: ");
            if (scanner.hasNextInt()) {
                bufferSize = scanner.nextInt();
                if (bufferSize > 0) {
                    break; // valid input
                } else {
                    System.out.println("Please enter a positive integer.");
                }
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                scanner.next(); // clear invalid input
            }
        }

        byte[] buffer = null;

        try {
            // Memory Allocation
            buffer = new byte[bufferSize];
            System.out.println("Buffer allocated of size: " + bufferSize);

            // Secure Random Number Generation
            secureRandom.nextBytes(buffer);
            System.out.println("Random bytes generated and stored in the buffer.");

            // Use the buffer for sensitive data, here simply simulating usage
            System.out.println("Using the buffer for sensitive data...");

        } catch (OutOfMemoryError e) {
            System.err.println("Memory allocation failed: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            // Memory Deallocation
            if (buffer != null) {
                // Zeroing the buffer before deallocation
                for (int i = 0; i < buffer.length; i++) {
                    buffer[i] = 0; // Zeroing the memory
                }
                buffer = null; // Allow garbage collection
                System.out.println("Buffer memory zeroed and deallocated.");
            }
        }

        scanner.close();
    }
}
