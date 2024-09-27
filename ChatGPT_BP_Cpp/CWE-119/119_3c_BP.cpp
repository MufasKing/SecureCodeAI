#include <iostream>
#include <stdexcept>
#include <cstdlib> // for std::strtol
#include <climits> // for INT_MAX and INT_MIN

int main(int argc, char* argv[]) {
    // Ensure there are at least two arguments: the program name and an index
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <index>" << std::endl;
        return 1; // Return non-zero for error
    }

    // Perform input validation on the index argument
    char* endptr;
    long index = std::strtol(argv[1], &endptr, 10);

    // Check if the conversion succeeded and ensure it's a valid integer
    if (*endptr != '\0' || endptr == argv[1]) {
        std::cerr << "Error: Invalid index. Please enter a valid integer." << std::endl;
        return 1;
    }

    // Check for out-of-range errors
    if (index < 1 || index > INT_MAX) {
        std::cerr << "Error: Index out of valid range. Enter a positive integer within range." << std::endl;
        return 1;
    }

    // Convert 1-based index to 0-based for array lookup
    int arg_index = static_cast<int>(index);

    // Ensure the index is within the number of provided arguments
    if (arg_index >= argc) {
        std::cerr << "Error: Index exceeds the number of arguments." << std::endl;
        return 1;
    }

    // Output the argument securely
    std::cout << "Argument at index " << index << ": " << argv[arg_index] << std::endl;

    return 0;
}
