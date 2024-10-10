#include <iostream>
#include <cstdlib>
#include <cstdio>

int main() {
    // Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // Generate three random floats
    float num1 = static_cast<float>(rand()) / RAND_MAX;
    float num2 = static_cast<float>(rand()) / RAND_MAX;
    float num3 = static_cast<float>(rand()) / RAND_MAX;

    // Buffers to hold the string representations
    char string[50];
    char string2[50];
    char string3[50];

    // Convert floats to strings
    sprintf(string, "%f", num1);
    sprintf(string2, "%f", num2);
    sprintf(string3, "%f", num3);

    // Output the strings
    std::cout << "String 1: " << string << std::endl;
    std::cout << "String 2: " << string2 << std::endl;
    std::cout << "String 3: " << string3 << std::endl;

    return 0;
}