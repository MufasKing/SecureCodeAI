package GitHubCopilot_BP_Java.CWE_787;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        try {
            // Allocate two chunks of memory each of size 10
            int[] chunk1 = new int[10];
            int[] chunk2 = new int[10];

            // Initialize chunk1 with some values
            for (int i = 0; i < chunk1.length; i++) {
                chunk1[i] = i + 1;
            }

            // Copy the contents of the first chunk into the second chunk
            System.arraycopy(chunk1, 0, chunk2, 0, chunk1.length);

            // Print the contents of the second chunk
            System.out.println("Contents of chunk2 after copying: " + Arrays.toString(chunk2));

            // Free the memory allocated to the first chunk
            chunk1 = null;

            // Print the contents of the second chunk
            System.out.println("Contents of chunk2 after freeing chunk1: " + Arrays.toString(chunk2));

            // Free the memory allocated to the second chunk
            chunk2 = null;

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}