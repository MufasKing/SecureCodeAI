#include <iostream>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()

int main() {
    // Initialize random seed
    srand(static_cast<unsigned int>(time(0)));

    // Generate three random integers larger than 1000
    int a = rand() % 9000 + 1001;  // Ensures the random number is between 1001 and 9999
    int b = rand() % 9000 + 1001;
    int c = rand() % 9000 + 1001;

    // Print the three integers
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << "c : " << c << std::endl;

    // Add the three integers
    int sum = a + b + c;

    // Print the sum using int
    std::cout << "sum: " << sum << std::endl;

    // Add the three integers using a long long
    long long sum2 = static_cast<long long>(a) + static_cast<long long>(b) + static_cast<long long>(c);

    // Print the sum using long long
    std::cout << "sum2: " << sum2 << std::endl;

    return 0;
}
