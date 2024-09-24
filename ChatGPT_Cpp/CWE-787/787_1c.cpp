#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstdio>

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Generate three random floats in the range [0.0, 1.0)
    float randomFloat1 = static_cast<float>(std::rand()) / RAND_MAX;
    float randomFloat2 = static_cast<float>(std::rand()) / RAND_MAX;
    float randomFloat3 = static_cast<float>(std::rand()) / RAND_MAX;

    // Variables to hold the resulting strings
    char string[50];
    char string2[50];
    char string3[50];

    // Convert floats to strings using sprintf
    std::sprintf(string, "%.4f", randomFloat1);
    std::sprintf(string2, "%.4f", randomFloat2);
    std::sprintf(string3, "%.4f", randomFloat3);

    // Output the results
    std::cout << "Random Float 1: " << string << std::endl;
    std::cout << "Random Float 2: " << string2 << std::endl;
    std::cout << "Random Float 3: " << string3 << std::endl;

    return 0;
}
