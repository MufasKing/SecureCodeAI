#include <iostream>
#include <cstdlib> // For std::atoi
#include <cstring> // For std::memset

int main(int argc, char* argv[]) {
    // Step 1: Input Validation
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <buffer_size>" << std::endl;
        return 1;
    }

    int bufferSize = std::atoi(argv[1]);
    if (bufferSize <= 0) {
        std::cerr << "Error: Buffer size must be a positive integer." << std::endl;
        return 1;
    }

    // Step 2: Dynamic Memory Allocation
    char* buffer = new(std::nothrow) char[bufferSize];
    if (!buffer) {
        std::cerr << "Error: Memory allocation failed." << std::endl;
        return 1;
    }

    // Step 3: Secure Buffer Initialization
    std::memset(buffer, 0, bufferSize);

    // Step 4: Safe Printing
    std::cout << "Buffer contents: ";
    for (int i = 0; i < bufferSize; ++i) {
        std::cout << static_cast<int>(buffer[i]) << " ";
    }
    std::cout << std::endl;

    // Step 5: Memory Deallocation
    delete[] buffer;

    return 0;
}