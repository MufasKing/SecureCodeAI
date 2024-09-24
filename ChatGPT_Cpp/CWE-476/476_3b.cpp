#include <iostream>
#include <cstdio>
#include <cstring>

int scan(char* buffer, size_t size) {
    if (buffer == nullptr || size == 0) {
        return 0; // Invalid buffer or size
    }

    // Use fgets to read input until newline or EOF
    if (fgets(buffer, size, stdin) != nullptr) {
        // Remove the newline character if it exists
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len - 1] == '\n') {
            buffer[len - 1] = '\0'; // Replace newline with null terminator
            return len - 1; // Return number of characters read, excluding newline
        }
        return len; // Return total length if no newline was found
    }
    
    return 0; // Return 0 if EOF or error
}

int main() {
    char buffer[1024]; // Buffer for input

    std::cout << "Enter a string (max 1023 characters): ";
    int charsRead = scan(buffer, sizeof(buffer));
    
    std::cout << "You entered: \"" << buffer << "\"\n";
    std::cout << "Number of characters read (excluding newline): " << charsRead << "\n";

    return 0;
}
