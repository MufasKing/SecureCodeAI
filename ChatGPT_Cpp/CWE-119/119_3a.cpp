#include <iostream>
#include <cstdlib>  // For atoi

int main(int argc, char* argv[]) {
    // Check if there are enough arguments
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <index> <arguments...>" << std::endl;
        return 1; // Return non-zero to indicate an error
    }

    // Convert the second argument (at index 1) to an integer
    int index = atoi(argv[1]);

    // Check if index is within bounds of the provided arguments
    if (index < 2 || index >= argc) {
        std::cerr << "Error: Invalid index" << std::endl;
        return 1; // Return non-zero to indicate an error
    }

    // Print the argument at the specified index
    std::cout << argv[index] << std::endl;

    return 0;
}
