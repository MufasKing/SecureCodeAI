import java.util.InputMismatchException;

public class SecureBuffer {
    
    private static final int MAX_BUFFER_SIZE = 1024; // Define a reasonable maximum buffer size

    public static void main(String[] args) {
        // Validate input
        if (args.length != 1) {
            System.err.println("Usage: java SecureBuffer <buffer_size>");
            System.exit(1);
        }

        int bufferSize = 0;

        try {
            // Parse and validate buffer size
            bufferSize = Integer.parseInt(args[0]);

            // Check buffer size range
            if (bufferSize <= 0 || bufferSize > MAX_BUFFER_SIZE) {
                throw new IllegalArgumentException("Buffer size must be a positive integer and less than or equal to " + MAX_BUFFER_SIZE);
            }
        } catch (NumberFormatException | IllegalArgumentException e) {
            System.err.println("Invalid buffer size: " + e.getMessage());
            System.exit(1);
        }

        // Securely allocate the buffer
        char[] buffer = new char[bufferSize];
        
        // Securely initialize the buffer (fill with a safe value)
        for (int i = 0; i < buffer.length; i++) {
            buffer[i] = '\u0000'; // Initialize to null character
        }

        // Print the contents of the buffer safely
        System.out.println("Buffer contents: " + new String(buffer));

        // Securely clear the buffer before deallocation
        clearBuffer(buffer);

        // Optionally, set to null for garbage collection (not strictly necessary)
        buffer = null;
    }

    // Securely clear the buffer to prevent sensitive data leakage
    private static void clearBuffer(char[] buffer) {
        if (buffer != null) {
            for (int i = 0; i < buffer.length; i++) {
                buffer[i] = '\u0000'; // Overwrite with null character
            }
        }
    }
}
