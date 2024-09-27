#include <iostream>
#include <cstring>  // for memcpy, memset
#include <stdexcept> // for std::invalid_argument

const size_t BUFFER_SIZE = 256;  // Define buffer size

// Memory copy function with safety checks
void safeMemoryCopy(void* dest, const void* src, size_t numBytes) {
    // Null pointer check
    if (dest == nullptr || src == nullptr) {
        throw std::invalid_argument("Null pointer passed as argument.");
    }

    // Buffer size check
    if (numBytes > BUFFER_SIZE) {
        throw std::out_of_range("Number of bytes to copy exceeds buffer size.");
    }

    // Use memory-safe function (memmove) instead of memcpy
    // memmove allows overlapping memory regions
    std::memmove(dest, src, numBytes);

    // Ensure that the destination buffer is null-terminated
    if (numBytes < BUFFER_SIZE) {
        static_cast<char*>(dest)[numBytes] = '\0';
    }
}

int main() {
    // Define source and destination buffers
    char source[BUFFER_SIZE] = "Hello, World!";  // Example source message
    char destination[BUFFER_SIZE];               // Destination buffer

    try {
        // Perform memory copy
        safeMemoryCopy(destination, source, strlen(source));

        // Output the copied content
        std::cout << "Copied message: " << destination << std::endl;
    } catch (const std::exception& e) {
        // Handle any errors
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
