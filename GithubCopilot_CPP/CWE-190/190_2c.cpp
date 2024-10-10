#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Initialize random seed
    std::srand(std::time(0));

    // Generate two random integers between 10 and 1000
    int num1 = std::rand() % 991 + 10;
    int num2 = std::rand() % 991 + 10;

    // Calculate the difference
    int difference = num1 - num2;

    // Print the results
    std::cout << "First random number: " << num1 << std::endl;
    std::cout << "Second random number: " << num2 << std::endl;
    std::cout << "Difference: " << difference << std::endl;

    return 0;
}