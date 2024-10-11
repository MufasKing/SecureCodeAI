import java.util.InputMismatchException;
import java.util.Scanner;

public class StackBufferExample {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int bufferSize = 0;

        // Input Validation
        while (true) {
            try {
                System.out.print("Enter the buffer size (positive integer): ");
                bufferSize = scanner.nextInt();

                if (bufferSize <= 0) {
                    System.out.println("Buffer size must be a positive integer. Please try again.");
                } else {
                    break; // Valid input, exit the loop
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a positive integer.");
                scanner.next(); // Clear the invalid input
            }
        }

        // Stack-based allocation of the buffer
        char[] buffer = new char[bufferSize];

        // Overwrite all values in the buffer with 'A'
        fillBufferWithA(buffer);

        // Output the buffer content
        System.out.print("Buffer content: ");
        for (char c : buffer) {
            System.out.print(c);
        }
        System.out.println();

        // Close the scanner
        scanner.close();
    }

    // Function to fill the buffer with 'A'
    private static void fillBufferWithA(char[] buffer) {
        for (int i = 0; i < buffer.length; i++) {
            buffer[i] = 'A';
        }
    }
}
