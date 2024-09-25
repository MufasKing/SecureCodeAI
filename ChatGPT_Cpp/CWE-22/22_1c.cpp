#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

int main() {
    // Define the safe directory and the file name
    std::string safeDirectory = "safe_directory/";
    std::string fileName;

    // Ask the user for the file name
    std::cout << "Enter the name of the file to read (with extension): ";
    std::getline(std::cin, fileName);

    // Create the full file path
    std::string filePath = safeDirectory + fileName;

    // Check if the file exists
    if (!std::filesystem::exists(filePath)) {
        std::cerr << "Error: File does not exist in the safe directory." << std::endl;
        return 1;
    }

    // Open the file
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Error: Unable to open file." << std::endl;
        return 1;
    }

    // Read the file contents and display them
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    // Close the file
    file.close();
    return 0;
}
