#include <iostream>

// Assume getMonthlySales is defined elsewhere
int getMonthlySales(int month);

int main() {
    int sum = 0;

    for (int i = 0; i < 3; ++i) {
        sum += getMonthlySales(i);
    }

    std::cout << "Total sales for the first quarter: " << sum << std::endl;
    return 0;
}