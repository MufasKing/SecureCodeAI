#include <iostream>

using namespace std;

// Function prototype for getMonthlySales
double getMonthlySales(int month);

int main() {
    double sum = 0.0;  // Initialize sum to 0

    // Loop iterates 3 times (i = 0, 1, 2)
    for (int i = 0; i < 3; i++) {
        sum += getMonthlySales(i);  // Add the sales for each month to sum
    }

    // After the loop, sum contains total sales for the first quarter
    cout << "Total sales for the first quarter: " << sum << endl;

    return 0;
}

// Dummy implementation of getMonthlySales
double getMonthlySales(int month) {
    // In a real application, this function would return the sales for the given month
    // Here we're using dummy values for demonstration
    return 1000.0 + (month * 100);  // Example: sales increase by 100 each month
}
