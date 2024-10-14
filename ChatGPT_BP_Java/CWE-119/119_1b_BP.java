public class MemoryCopyUtil {

    /**
     * Copies bytes from source to destination safely.
     *
     * @param dest  The destination byte array where data will be copied.
     * @param src   The source byte array from where data is to be copied.
     * @param numBytes The number of bytes to copy.
     * @throws IllegalArgumentException if input validation fails.
     * @throws ArrayIndexOutOfBoundsException if boundary checks fail.
     */
    public static void memcpy(byte[] dest, byte[] src, int numBytes) throws IllegalArgumentException, ArrayIndexOutOfBoundsException {
        // Input validation
        if (dest == null || src == null) {
            throw new IllegalArgumentException("Source or destination cannot be null.");
        }

        if (numBytes < 0) {
            throw new IllegalArgumentException("Number of bytes to copy cannot be negative.");
        }

        // Boundary checking and buffer size validation
        if (numBytes > src.length) {
            throw new ArrayIndexOutOfBoundsException("Number of bytes to copy exceeds source length.");
        }

        if (numBytes > dest.length) {
            throw new ArrayIndexOutOfBoundsException("Number of bytes to copy exceeds destination buffer size.");
        }

        // Secure copying
        for (int i = 0; i < numBytes; i++) {
            dest[i] = src[i];
        }
    }

    /**
     * Returns the length of a string in bytes.
     *
     * @param str The string whose length is to be calculated.
     * @return The length of the string.
     * @throws IllegalArgumentException if the string is null.
     */
    public static int strlen(String str) throws IllegalArgumentException {
        if (str == null) {
            throw new IllegalArgumentException("Input string cannot be null.");
        }
        return str.length();
    }

    /**
     * Copies a message to a buffer after performing necessary validations.
     *
     * @param message The message to copy.
     * @param buffer  The buffer where the message is to be copied.
     * @throws IllegalArgumentException if the message or buffer is invalid.
     */
    public static void copyMessageToBuffer(String message, byte[] buffer) throws IllegalArgumentException {
        if (message == null || buffer == null) {
            throw new IllegalArgumentException("Message or buffer cannot be null.");
        }

        byte[] messageBytes = message.getBytes(); // Convert string to bytes
        int messageLength = strlen(message);

        // Check if buffer can accommodate the message
        if (messageLength > buffer.length) {
            throw new IllegalArgumentException("Buffer size is too small to hold the message.");
        }

        // Perform the copy
        memcpy(buffer, messageBytes, messageLength);
    }

    public static void main(String[] args) {
        try {
            String message = "Hello, World!";
            byte[] buffer = new byte[50]; // Destination buffer
            copyMessageToBuffer(message, buffer);

            // Convert buffer back to string to verify the copy
            String copiedMessage = new String(buffer, 0, strlen(message));
            System.out.println("Copied message: " + copiedMessage);

        } catch (IllegalArgumentException | ArrayIndexOutOfBoundsException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
