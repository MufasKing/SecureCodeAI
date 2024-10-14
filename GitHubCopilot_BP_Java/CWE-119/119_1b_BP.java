package GitHubCopilot_BP_Java.CWE_119;

public class Main {

    // Function to copy bytes from source to destination
    public static void memcpy(byte[] dest, byte[] src, int numBytes) throws IllegalArgumentException {
        if (dest == null || src == null) {
            throw new IllegalArgumentException("Source or destination cannot be null");
        }
        if (numBytes < 0 || numBytes > src.length || numBytes > dest.length) {
            throw new IllegalArgumentException("Invalid number of bytes to copy");
        }
        for (int i = 0; i < numBytes; i++) {
            dest[i] = src[i];
        }
    }

    // Function to get the length of a string
    public static int strlen(String str) {
        if (str == null) {
            return 0;
        }
        return str.length();
    }

    // Function to copy message to buffer with validation and error handling
    public static void copyMessageToBuffer(String message, byte[] buffer) {
        if (message == null || buffer == null) {
            throw new IllegalArgumentException("Message or buffer cannot be null");
        }

        int messageLength = strlen(message);
        if (messageLength > buffer.length) {
            throw new IllegalArgumentException("Buffer size is too small for the message");
        }

        byte[] messageBytes = message.getBytes();
        memcpy(buffer, messageBytes, messageLength);
    }

    public static void main(String[] args) {
        try {
            String message = "Hello, World!";
            byte[] buffer = new byte[20];
            copyMessageToBuffer(message, buffer);
            System.out.println("Message copied to buffer successfully.");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}