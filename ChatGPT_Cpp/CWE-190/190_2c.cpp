#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator
    std::srand(std::time(0));

    // Generate two random integers between 10 and 1000
    int num1 = std::rand() % 991 + 10; // 991 is the range (1000 - 10 + 1)
    int num2 = std::rand() % 991 + 10;

    // Calculate the difference
    int difference = num1 - num2;

    // Print the results
    std::cout << "First number: " << num1 << std::endl;
    std::cout << "Second number: " << num2 << std::endl;
    std::cout << "Difference: " << difference << std::endl;

    return 0;
}
