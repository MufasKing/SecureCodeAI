#include <iostream>
#include <cstdio>  // For fgets
#include <cstdlib> // For malloc and free

int main() {
    // Allocate a buffer of 1024 bytes
    char* buf = (char*)malloc(1024 * sizeof(char));
    if (buf == nullptr) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return 1; // Exit if memory allocation fails
    }

    std::cout << "Please enter up to 10 characters: ";

    // Read 10 characters from standard input
    if (fgets(buf, 11, stdin) != nullptr) {
        std::cout << "You entered: " << buf << std::endl;
    } else {
        std::cerr << "Error reading input!" << std::endl;
    }

    // Free allocated memory
    free(buf);
    return 0;
}
