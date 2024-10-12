public class Main {
    public static void main(String[] args) {
        try {
            allocateAndOverwriteBuffer(10); // Example buffer size
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static void allocateAndOverwriteBuffer(int buffer_size) throws IllegalArgumentException {
        // Input Validation
        if (buffer_size <= 0) {
            throw new IllegalArgumentException("Buffer size must be positive.");
        }

        // Stack-based allocation
        char[] buffer = new char[buffer_size];

        // Overwrite all values in the buffer with 'A'
        for (int i = 0; i < buffer_size; i++) {
            buffer[i] = 'A';
        }

        // Output the buffer for verification
        System.out.println(buffer);
    }
}