import java.util.Arrays;

public class MemoryManagementSimulation {

    public static void main(String[] args) {
        try {
            // Step 1: Memory Allocation
            int size = 10;
            int[] chunk1 = new int[size]; // Allocating the first chunk
            int[] chunk2 = new int[size]; // Allocating the second chunk
            
            // Step 2: Initialize chunk1 with some values
            for (int i = 0; i < chunk1.length; i++) {
                chunk1[i] = i + 1; // Initializing with values 1 to 10
            }

            // Print initial values of chunk1
            System.out.println("Initial values of chunk1: " + Arrays.toString(chunk1));

            // Step 3: Memory Copying
            System.arraycopy(chunk1, 0, chunk2, 0, chunk1.length); // Copying contents from chunk1 to chunk2
            
            // Print values of chunk2 after copying
            System.out.println("Values of chunk2 after copying: " + Arrays.toString(chunk2));

            // Step 4: Memory Zeroing (Secure practice)
            Arrays.fill(chunk1, 0); // Zero out chunk1 to clear sensitive data
            
            // Print values after zeroing
            System.out.println("Values of chunk1 after zeroing: " + Arrays.toString(chunk1));

            // Step 5: Memory Freeing
            chunk1 = null; // Freeing the first chunk
            chunk2 = null; // Freeing the second chunk
            
            // Optional: Suggest garbage collection (not guaranteed)
            System.gc(); 

            System.out.println("Memory freed. Set chunk1 and chunk2 to null.");

        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}

