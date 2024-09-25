#include <iostream>
#include <fstream>
#include <string>

int main() {
    // Define the path to the file
    std::string filePath = "/safe/your_file.txt";

    // Create an input file stream
    std::ifstream file(filePath);

    // Check if the file was opened successfully
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file at " << filePath << std::endl;
        return 1;
    }

    // Read the file line by line
    std::string line;
    while (std::getline(file, line)) {
        // Output the line to the console
        std::cout << line << std::endl;
    }

    // Close the file
    file.close();

    return 0;
}
