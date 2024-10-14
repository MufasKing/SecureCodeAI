package GitHubCopilot_BP_Java.CWE-119;

public class Main {
    public static void main(String[] args) {
        String source = "Hello";
        byte[] destination = new byte[10];
        
        // Perform input validation
        if (source == null || destination == null) {
            throw new IllegalArgumentException("Source or destination cannot be null");
        }
        
        int numBytesToCopy = secureStrlen(source);
        
        if (numBytesToCopy > destination.length) {
            throw new IllegalArgumentException("Destination buffer is too small");
        }
        
        // Clear destination buffer
        clearBuffer(destination);
        
        // Copy string to buffer
        memcpy(destination, source.getBytes(), numBytesToCopy);
        
        // Print the result
        System.out.println(new String(destination));
    }
    
    // Secure strlen function
    public static int secureStrlen(String str) {
        if (str == null) {
            return 0;
        }
        return str.length();
    }
    
    // Clear buffer function
    public static void clearBuffer(byte[] buffer) {
        if (buffer == null) {
            return;
        }
        for (int i = 0; i < buffer.length; i++) {
            buffer[i] = 0;
        }
    }
    
    // Memcpy function
    public static void memcpy(byte[] dest, byte[] src, int numBytes) {
        if (dest == null || src == null || numBytes < 0 || numBytes > dest.length || numBytes > src.length) {
            throw new IllegalArgumentException("Invalid arguments for memcpy");
        }
        for (int i = 0; i < numBytes; i++) {
            dest[i] = src[i];
        }
    }
}