#include <iostream>

int main() {
    double totalSales = 0.0;
    
    double januarySales = 1000.0; // Example sales for January
    double februarySales = 1500.0; // Example sales for February
    double marchSales = 1200.0; // Example sales for March
    
    totalSales += januarySales;
    totalSales += februarySales;
    totalSales += marchSales;
    
    std::cout << "Total Sales: " << totalSales << std::endl;
    
    return 0;
}