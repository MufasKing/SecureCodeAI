#include <iostream>
#include <cstdlib>
#include <ctime>

int getMonthlySales() {
    return rand() % 100001; // Random number between 0 and 100000
}

int main() {
    srand(time(0)); // Seed for random number generation

    int monthlySales[12];
    for (int i = 0; i < 12; ++i) {
        monthlySales[i] = getMonthlySales();
    }

    int quarterlySales[4] = {0, 0, 0, 0};
    for (int i = 0; i < 12; ++i) {
        quarterlySales[i / 3] += monthlySales[i];
    }

    for (int i = 0; i < 4; ++i) {
        std::cout << "Sales for quarter " << (i + 1) << ": " << quarterlySales[i] << std::endl;
    }

    return 0;
}