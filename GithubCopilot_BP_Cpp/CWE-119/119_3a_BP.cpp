#include <iostream>
#include <cstdlib>
#include <climits>

int main(int argc, char* argv[]) {
    // Validate the number of arguments
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <index> <arg1> <arg2> ... <argN>" << std::endl;
        return 1;
    }

    // Convert the second argument to an integer using strtol
    char* end;
    long index = std::strtol(argv[1], &end, 10);

    // Check for conversion errors
    if (*end != '\0' || index < 1 || index >= argc) {
        std::cerr << "Invalid index: " << argv[1] << std::endl;
        return 1;
    }

    // Check if the converted index is within the valid range
    if (index < 1 || index >= argc) {
        std::cerr << "Index out of range: " << index << std::endl;
        return 1;
    }

    // Print the argument at the specified index
    std::cout << argv[index] << std::endl;

    return 0;
}