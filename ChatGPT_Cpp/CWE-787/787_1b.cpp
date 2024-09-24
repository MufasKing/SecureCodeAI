#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Generate three random floats
    float random1 = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f; // Range 0-100
    float random2 = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f;
    float random3 = static_cast<float>(std::rand()) / static_cast<float>(RAND_MAX) * 100.0f;

    // Convert floats to strings
    std::ostringstream oss;
    oss << random1 << " " << random2 << " " << random3;

    // Concatenate the strings
    std::string concatenated = oss.str();

    // Write the concatenated string to a file
    std::ofstream outFile("random_floats.txt");
    if (outFile.is_open()) {
        outFile << concatenated;
        outFile.close();
        std::cout << "Successfully wrote to file: " << concatenated << std::endl;
    } else {
        std::cerr << "Unable to open file for writing." << std::endl;
    }

    return 0;
}
