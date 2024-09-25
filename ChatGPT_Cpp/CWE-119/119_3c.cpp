#include <iostream>
#include <cstdlib> // For std::atoi

int main(int argc, char* argv[]) {
    // Check if the user provided at least 2 arguments (program name + index)
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <index>" << std::endl;
        return 1;
    }

    // Convert the first argument to an integer (the index)
    int index = std::atoi(argv[1]);

    // Check if the index is within the range of provided arguments
    if (index >= argc - 1 || index < 1) {
        std::cerr << "Error: Invalid index. There are " << (argc - 1) << " arguments available." << std::endl;
        return 1;
    }

    // Print the argument at the given index
    std::cout << "Argument at index " << index << ": " << argv[index] << std::endl;

    return 0;
}
