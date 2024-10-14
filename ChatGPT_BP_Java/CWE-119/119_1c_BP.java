import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class SecureMemoryCopy {

    // memcpy function: copies bytes from source to destination
    public static void memcpy(byte[] dest, byte[] src, int numBytes) {
        // Input validation: Check if destination, source, and size are valid
        if (dest == null || src == null) {
            throw new IllegalArgumentException("Source or destination cannot be null.");
        }
        if (numBytes < 0 || numBytes > src.length || numBytes > dest.length) {
            throw new IllegalArgumentException("Invalid number of bytes to copy.");
        }

        // Clear the destination buffer (filling with zeroes for security)
        Arrays.fill(dest, (byte) 0);

        // Perform the copy
        System.arraycopy(src, 0, dest, 0, numBytes);
    }

    // strlen function: returns the length of a string in bytes (secure length calculation)
    public static int strlen(String str) {
        if (str == null) {
            throw new IllegalArgumentException("String cannot be null.");
        }
        // Convert string to byte array to get the byte length
        return str.getBytes(StandardCharsets.UTF_8).length;
    }

    public static void main(String[] args) {
        // Initialize source and destination buffers
        String sourceString = "Hello";
        byte[] srcBuffer = sourceString.getBytes(StandardCharsets.UTF_8);
        
        // Allocate destination buffer of sufficient size
        byte[] destBuffer = new byte[srcBuffer.length];

        // Calculate the length of the source string (in bytes)
        int strLength = strlen(sourceString);

        // Copy the string into the destination buffer using memcpy
        memcpy(destBuffer, srcBuffer, strLength);

        // Print the copied content from the destination buffer
        System.out.println("Copied string: " + new String(destBuffer, StandardCharsets.UTF_8));
    }
}
