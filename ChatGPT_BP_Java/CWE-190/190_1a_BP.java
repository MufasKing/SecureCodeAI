import java.util.Scanner;

public class SecureInputHandling {

    public static void main(String[] args) {
        SecureInputHandling app = new SecureInputHandling();
        app.run();
    }

    public void run() {
        try {
            // Step 1: Read user input
            int userInput = readIntegerInput();

            // Step 2: Add 1000 with overflow/underflow checks
            int result = addWithOverflowCheck(userInput, 1000);

            // Step 3: Display the result securely
            System.out.printf("The result is: %d%n", result);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    // Method to read an integer from the command line with validation
    private int readIntegerInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer value: ");

        if (!scanner.hasNextInt()) {
            scanner.close();
            throw new IllegalArgumentException("Invalid input. Please enter a valid integer.");
        }

        int input = scanner.nextInt();
        scanner.close();
        return input;
    }

    // Method to add two integers and check for overflow/underflow
    private int addWithOverflowCheck(int a, int b) {
        if ((b > 0 && a > Integer.MAX_VALUE - b) || (b < 0 && a < Integer.MIN_VALUE - b)) {
            throw new IllegalArgumentException("Integer overflow/underflow detected.");
        }
        return a + b;
    }
}
