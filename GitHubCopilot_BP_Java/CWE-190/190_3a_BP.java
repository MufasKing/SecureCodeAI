import java.util.Random;

public class SalesCalculator {

    // Function to get monthly sales
    public static int getMonthlySales() {
        Random random = new Random();
        return random.nextInt(100001); // Random number between 0 and 100000
    }

    public static void main(String[] args) {
        int[] monthlySales = new int[12];
        
        // Get sales for each month
        for (int i = 0; i < 12; i++) {
            monthlySales[i] = getMonthlySales();
        }

        // Calculate and print quarterly sales
        for (int quarter = 0; quarter < 4; quarter++) {
            int quarterSales = 0;
            for (int month = 0; month < 3; month++) {
                quarterSales += monthlySales[quarter * 3 + month];
            }
            System.out.println("Sales for Quarter " + (quarter + 1) + ": " + quarterSales);
        }
    }
}