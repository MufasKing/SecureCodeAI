#include <iostream>
#include <cstring>

void copyBytes(char* dest, const char* src, size_t numBytes) {
    // Ensure we do not copy more than 256 bytes
    if (numBytes > 256) {
        numBytes = 256;
    }

    // Copy bytes from src to dest
    for (size_t i = 0; i < numBytes; ++i) {
        dest[i] = src[i];
    }
}

int main() {
    char buffer[256] = {0}; // Destination buffer
    const char* message = "Hello, World!"; // Source message

    // Copy the message to the buffer
    copyBytes(buffer, message, strlen(message) + 1); // +1 to include the null terminator

    // Print the copied message
    std::cout << "Copied message: " << buffer << std::endl;

    return 0;
}