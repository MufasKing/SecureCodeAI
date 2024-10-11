public class SalesCalculator {

    // Method to get monthly sales for a given month
    public int getMonthlySales(int month) {
        // Placeholder for actual sales logic
        // In a real scenario, this might fetch data from a database or an API
        return 1000 * (month + 1); // Example sales data
    }

    // Method to calculate total sales for the first quarter
    public int calculateFirstQuarterSales() {
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            sum += getMonthlySales(i);
        }
        return sum;
    }

    public static void main(String[] args) {
        SalesCalculator calculator = new SalesCalculator();
        int firstQuarterSales = calculator.calculateFirstQuarterSales();
        System.out.println("Total sales for the first quarter: " + firstQuarterSales);
    }
}