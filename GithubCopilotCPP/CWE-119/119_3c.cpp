#include <iostream>
#include <cstdlib> // For std::atoi

int main(int argc, char* argv[]) {
    // Check if at least two arguments are provided (program name and index)
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <index>" << std::endl;
        return 1;
    }

    // Convert the index argument to an integer
    int index = std::atoi(argv[1]);

    // Check if the index is within the valid range
    if (index < 1 || index >= argc) {
        std::cerr << "Error: Index out of range." << std::endl;
        return 1;
    }

    // Print the corresponding command line argument
    std::cout << argv[index] << std::endl;

    return 0;
}