#include <iostream>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()

// Function to simulate getting monthly sales (returns a random number between 0 and 100000)
int getMonthlySales() {
    return rand() % 100001;  // Random number between 0 and 100000
}

int main() {
    // Seed random number generator
    srand(static_cast<unsigned int>(time(0)));

    int quarterlySales[4] = {0};  // Array to store the sales for each quarter

    // Call getMonthlySales 12 times (once for each month) and add up the quarterly sales
    for (int month = 0; month < 12; ++month) {
        int sales = getMonthlySales();
        std::cout << "Month " << (month + 1) << " sales: " << sales << std::endl;

        // Determine which quarter the month belongs to and add the sales to the corresponding quarter
        int quarter = month / 3;
        quarterlySales[quarter] += sales;
    }

    // Print the quarterly sales
    for (int q = 0; q < 4; ++q) {
        std::cout << "Quarter " << (q + 1) << " total sales: " << quarterlySales[q] << std::endl;
    }

    return 0;
}
