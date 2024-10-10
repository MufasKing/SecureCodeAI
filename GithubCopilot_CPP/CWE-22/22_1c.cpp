#include <iostream>
#include <fstream>
#include <string>

// Function to read a file from a safe directory
void readFileFromSafeDirectory(const std::string& filename) {
    // Define the safe directory path
    const std::string safeDirectory = "/path/to/safe/directory/";

    // Construct the full file path
    std::string filePath = safeDirectory + filename;

    // Open the file
    std::ifstream file(filePath);

    // Check if the file is open
    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file " << filePath << std::endl;
        return;
    }

    // Read the file content
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    // Close the file
    file.close();
}

int main() {
    // Example usage
    std::string filename;
    std::cout << "Enter the filename to read: ";
    std::cin >> filename;

    readFileFromSafeDirectory(filename);

    return 0;
}