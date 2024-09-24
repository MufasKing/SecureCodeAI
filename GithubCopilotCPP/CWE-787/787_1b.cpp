#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Generate 3 random floats
    float num1 = static_cast<float>(std::rand()) / RAND_MAX;
    float num2 = static_cast<float>(std::rand()) / RAND_MAX;
    float num3 = static_cast<float>(std::rand()) / RAND_MAX;

    // Convert floats to strings
    std::ostringstream oss;
    oss << num1 << " " << num2 << " " << num3;

    // Concatenate the strings
    std::string concatenatedString = oss.str();

    // Write the string to a file
    std::ofstream outFile("output.txt");
    if (outFile.is_open()) {
        outFile << concatenatedString;
        outFile.close();
        std::cout << "Successfully wrote to the file." << std::endl;
    } else {
        std::cerr << "Unable to open file." << std::endl;
    }

    return 0;
}