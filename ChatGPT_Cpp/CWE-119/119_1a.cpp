#include <iostream>
#include <cstring>  // For memcpy function

// Function to copy bytes from one memory location to another
void copyMemory(void* dest, const void* src, size_t numBytes) {
    // Ensure that the number of bytes does not exceed the buffer size
    const size_t bufferSize = 256;

    if (numBytes > bufferSize) {
        std::cerr << "Error: Cannot copy more than 256 bytes." << std::endl;
        return;
    }

    // Perform the memory copy
    std::memcpy(dest, src, numBytes);
}

int main() {
    // Example usage

    // Source and destination buffers
    char source[256] = "This is the message to copy!";
    char destination[256] = {};

    // Copy memory from source to destination
    copyMemory(destination, source, strlen(source) + 1);  // +1 to include the null terminator

    // Print the result
    std::cout << "Copied message: " << destination << std::endl;

    return 0;
}
