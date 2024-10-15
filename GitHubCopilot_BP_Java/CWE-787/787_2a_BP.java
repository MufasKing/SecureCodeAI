package GitHubCopilot_BP_Java.CWE_787;

public class Main {
    public static void main(String[] args) {
        // Memory Allocation
        byte[] firstChunk = new byte[10];
        byte[] secondChunk = new byte[10];

        // Secure Data Source
        for (int i = 0; i < firstChunk.length; i++) {
            firstChunk[i] = (byte) (i + 1); // Example secure data
        }

        // Memory Copying
        System.arraycopy(firstChunk, 0, secondChunk, 0, firstChunk.length);

        // Printing Sensitive Data
        System.out.println("Contents of the second chunk:");
        for (byte b : secondChunk) {
            System.out.print(b + " ");
        }
        System.out.println();

        // Memory Deallocation
        firstChunk = null;
        secondChunk = null;
    }
}