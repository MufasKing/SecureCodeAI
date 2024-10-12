import java.util.Arrays;
import java.util.Base64;

public class SecureMemoryHandling {

    public static void main(String[] args) {
        // Step 1: Memory Allocation
        char[] chunk1 = new char[10];
        char[] chunk2 = new char[10];

        // Step 2: Secure Data Source (using a hardcoded secure string)
        String secureData = "SensitiveData";
        secureData = secureData.length() > 10 ? secureData.substring(0, 10) : secureData;

        // Fill the first chunk with secure data
        for (int i = 0; i < chunk1.length; i++) {
            chunk1[i] = secureData.charAt(i);
        }

        // Step 3: Memory Copying
        System.arraycopy(chunk1, 0, chunk2, 0, chunk1.length);

        // Step 4: Printing Sensitive Data (only after copying)
        printSensitiveData(chunk2);

        // Step 5: Memory Deallocation
        Arrays.fill(chunk1, '\0'); // Clear sensitive data
        Arrays.fill(chunk2, '\0'); // Clear sensitive data
    }

    // Method to print sensitive data securely
    private static void printSensitiveData(char[] data) {
        // Convert to String for printing
        String dataToPrint = new String(data);
        // Use Base64 encoding to avoid direct exposure
        String encodedData = Base64.getEncoder().encodeToString(dataToPrint.getBytes());
        System.out.println("Encoded sensitive data: " + encodedData);
    }
}
