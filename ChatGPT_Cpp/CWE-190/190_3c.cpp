#include <iostream>

int main() {
    // Declare a variable to hold total sales
    double totalSales = 0.0;

    // Add sales for each month
    double januarySales = 1200.50;
    double februarySales = 980.75;
    double marchSales = 1350.00;

    totalSales += januarySales;   // Adding January sales
    totalSales += februarySales;  // Adding February sales
    totalSales += marchSales;     // Adding March sales

    // Print the total sales to the screen
    std::cout << "Total Sales: $" << totalSales << std::endl;

    return 0;
}
