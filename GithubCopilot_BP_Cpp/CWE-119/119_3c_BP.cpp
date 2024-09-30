#include <iostream>
#include <cstdlib>
#include <cstring>

int main(int argc, char* argv[]) {
    // Check if the index argument is provided
    if (argc < 2) {
        std::cerr << "Error: No index provided." << std::endl;
        return 1;
    }

    // Convert the index argument to an integer
    char* end;
    long index = std::strtol(argv[1], &end, 10);

    // Check if the conversion was successful and the index is a valid number
    if (*end != '\0' || index < 1) {
        std::cerr << "Error: Invalid index provided." << std::endl;
        return 1;
    }

    // Check if the index is within the range of provided arguments
    if (index >= argc) {
        std::cerr << "Error: Index out of range." << std::endl;
        return 1;
    }

    // Print the corresponding argument
    std::cout << "Argument at index " << index << ": " << argv[index] << std::endl;

    return 0;
}