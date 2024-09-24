#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>

std::string floatToString(float number) {
    std::ostringstream oss;
    oss << number;
    return oss.str();
}

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(0)));

    // Generate three random floats
    float a = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f; // Random float between 0 and 100
    float b = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f;
    float c = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f;

    // Convert floats to strings
    std::string str_a = floatToString(a);
    std::string str_b = floatToString(b);
    std::string str_c = floatToString(c);

    // Output the results
    std::cout << "Random floats as strings:\n";
    std::cout << "str_a: " << str_a << "\n";
    std::cout << "str_b: " << str_b << "\n";
    std::cout << "str_c: " << str_c << "\n";

    return 0;
}
