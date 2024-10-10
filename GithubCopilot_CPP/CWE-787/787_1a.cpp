#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

// Function to convert float to string
std::string floatToString(float value) {
    return std::to_string(value);
}

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(0)));

    // Generate three random floats
    float a = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX);
    float b = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX);
    float c = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX);

    // Convert floats to strings
    std::string str_a = floatToString(a);
    std::string str_b = floatToString(b);
    std::string str_c = floatToString(c);

    // Output the results
    std::cout << "str_a: " << str_a << std::endl;
    std::cout << "str_b: " << str_b << std::endl;
    std::cout << "str_c: " << str_c << std::endl;

    return 0;
}