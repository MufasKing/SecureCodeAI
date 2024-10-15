public class main {
    public static void main(String[] args) {
        // Declare a variable called totalSales
        double totalSales = 0.0;

        // Add the sales for each month to the totalSales variable
        double januarySales = 1000.50; // Example sales for January
        double februarySales = 1200.75; // Example sales for February
        double marchSales = 1100.25; // Example sales for March

        totalSales += januarySales;
        totalSales += februarySales;
        totalSales += marchSales;

        // Print the total sales to the screen
        System.out.printf("Total Sales: $%.2f%n", totalSales);
    }
}