#include <iostream>
#include <cstdlib> // for malloc and free
#include <cstring> // for strncpy

int main() {
    // Allocate the first buffer
    char* buf = static_cast<char*>(malloc(1024 * sizeof(char)));
    if (buf == nullptr) {
        std::cerr << "Memory allocation failed for buf." << std::endl;
        return 1;
    }

    // Read 100 characters from stdin into buf
    std::cout << "Enter input for first buffer (max 100 characters): ";
    fgets(buf, 1024, stdin); // Read up to 1024 characters

    // Allocate the second buffer
    char* buf1 = static_cast<char*>(malloc(1024 * sizeof(char)));
    if (buf1 == nullptr) {
        std::cerr << "Memory allocation failed for buf1." << std::endl;
        free(buf); // Free the first buffer before exiting
        return 1;
    }

    // Read 100 characters from stdin into buf1
    std::cout << "Enter input for second buffer (max 100 characters): ";
    fgets(buf1, 1024, stdin); // Read up to 1024 characters

    // Copy the first 100 characters from buf to buf1
    char temp[101]; // Temp buffer to hold 100 characters + null terminator
    strncpy(temp, buf, 100);
    temp[100] = '\0'; // Ensure null termination
    std::cout << "Copied first 100 characters: " << temp << std::endl;

    // Print second buffer
    std::cout << "Content of the second buffer: " << buf1 << std::endl;

    // Free allocated memory
    free(buf);
    free(buf1);

    return 0;
}
