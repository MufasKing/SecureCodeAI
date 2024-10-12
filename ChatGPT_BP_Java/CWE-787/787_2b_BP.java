public class MemoryManagement {

    public static void main(String[] args) {
        try {
            // Step 1: Allocate two chunks of memory (arrays of size 10)
            int[] firstChunk = new int[10];
            int[] secondChunk = new int[10];

            // Step 2: Initialize the first chunk with some values
            for (int i = 0; i < firstChunk.length; i++) {
                firstChunk[i] = i + 1; // Example initialization
            }

            // Step 3: Copy the contents of the first chunk into the second chunk
            System.arraycopy(firstChunk, 0, secondChunk, 0, firstChunk.length);

            // Step 4: Print the contents of the second chunk
            System.out.println("Contents of the second chunk after copying:");
            printChunk(secondChunk);

            // Step 5: Free the memory allocated to the first chunk (set to null)
            firstChunk = null;
            System.out.println("First chunk memory freed.");

            // Step 6: Print the contents of the second chunk again
            System.out.println("Contents of the second chunk after freeing the first chunk:");
            printChunk(secondChunk);

            // Step 7: Free the memory allocated to the second chunk (set to null)
            secondChunk = null;
            System.out.println("Second chunk memory freed.");

        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to print the contents of a chunk
    private static void printChunk(int[] chunk) {
        if (chunk == null) {
            System.out.println("The chunk is empty (null reference).");
            return;
        }
        for (int value : chunk) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}

