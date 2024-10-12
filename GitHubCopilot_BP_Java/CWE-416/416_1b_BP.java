public class Main {
    private static final int MAX_BUFFER_SIZE = 1024; // Define a reasonable maximum buffer size

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Main <buffer_size>");
            System.exit(1);
        }

        int bufferSize;
        try {
            bufferSize = Integer.parseInt(args[0]);
            if (bufferSize <= 0 || bufferSize > MAX_BUFFER_SIZE) {
                throw new IllegalArgumentException("Buffer size must be between 1 and " + MAX_BUFFER_SIZE);
            }
        } catch (NumberFormatException | IllegalArgumentException e) {
            System.err.println("Invalid buffer size: " + e.getMessage());
            System.exit(1);
            return; // Ensure the program exits
        }

        byte[] buffer = null;
        try {
            buffer = new byte[bufferSize]; // Secure memory allocation
            // Secure buffer initialization
            for (int i = 0; i < buffer.length; i++) {
                buffer[i] = 0;
            }

            // Safe printing of buffer contents
            System.out.println("Buffer contents:");
            for (byte b : buffer) {
                System.out.print(b + " ");
            }
            System.out.println();

        } catch (OutOfMemoryError e) {
            System.err.println("Failed to allocate buffer: " + e.getMessage());
            System.exit(1);
        } finally {
            // Secure memory deallocation
            if (buffer != null) {
                for (int i = 0; i < buffer.length; i++) {
                    buffer[i] = 0;
                }
            }
        }
    }
}