#include <iostream>
#include <string>
#include <cstdlib>    // For atoi()
#include <stdexcept>  // For exceptions
#include <cerrno>     // For errno
#include <limits>     // For integer limits

// Function to safely convert a string to an integer
int safeStringToInt(const std::string& str) {
    errno = 0; // Reset errno before calling strtol
    char* endPtr = nullptr;
    long value = std::strtol(str.c_str(), &endPtr, 10);

    // Check if the entire string was converted and check for out-of-range errors
    if (*endPtr != '\0' || errno == ERANGE || value < std::numeric_limits<int>::min() || value > std::numeric_limits<int>::max()) {
        throw std::invalid_argument("Invalid integer input: " + str);
    }

    return static_cast<int>(value);
}

int main(int argc, char* argv[]) {
    try {
        // Check if at least two arguments are provided (program name + second argument)
        if (argc < 2) {
            std::cerr << "Error: No arguments provided.\n";
            return 1;
        }

        // Convert the second argument (at index 1) to an integer (this will be the index argument)
        int index = safeStringToInt(argv[1]);

        // Check if index is within valid range (between 1 and argc-1)
        if (index < 1 || index >= argc) {
            std::cerr << "Error: Index out of range. Must be between 1 and " << argc - 1 << ".\n";
            return 1;
        }

        // Print the argument at the specified index
        std::cout << "Argument at index " << index << ": " << argv[index] << std::endl;

        return 0; // Success
    } catch (const std::exception& ex) {
        // Handle any exceptions thrown during conversion or other operations
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1; // Return error code
    }
}
