import java.util.Scanner;

public class SalesCalculator {

    public static void main(String[] args) {
        // Declare the totalSales variable
        double totalSales = 0.0;

        // Scanner for user input
        Scanner scanner = new Scanner(System.in);

        // Input validation and addition of monthly sales
        for (int i = 1; i <= 3; i++) {
            double monthlySales = getMonthlySales(scanner, i);
            totalSales += monthlySales;
        }

        // Close the scanner to prevent resource leak
        scanner.close();

        // Print the total sales securely
        System.out.printf("The total sales are: %.2f%n", totalSales);
    }

    // Function to securely get monthly sales with input validation
    private static double getMonthlySales(Scanner scanner, int month) {
        double sales = 0.0;
        boolean validInput = false;

        while (!validInput) {
            System.out.printf("Enter the sales for month %d: ", month);

            if (scanner.hasNextDouble()) {
                sales = scanner.nextDouble();

                // Validate sales is non-negative
                if (sales >= 0) {
                    validInput = true;
                } else {
                    System.out.println("Sales cannot be negative. Please try again.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next(); // clear invalid input
            }
        }

        return sales;
    }
}
