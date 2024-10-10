#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator
    std::srand(std::time(0));

    // Generate three random integers larger than 1000
    int a = std::rand() % 9000 + 1000;
    int b = std::rand() % 9000 + 1000;
    int c = std::rand() % 9000 + 1000;

    // Print the three integers
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << "c : " << c << std::endl;

    // Add the three integers and print the result
    int sum = a + b + c;
    std::cout << "sum: " << sum << std::endl;

    // Add the three integers using a long long and print the result
    long long sum2 = static_cast<long long>(a) + b + c;
    std::cout << "sum2: " << sum2 << std::endl;

    return 0;
}