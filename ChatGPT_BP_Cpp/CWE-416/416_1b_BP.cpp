#include <iostream>
#include <cstring>  // For memset
#include <cstdlib>  // For std::malloc, std::free, std::atoi
#include <limits>   // For std::numeric_limits
#include <stdexcept> // For std::invalid_argument

// Constants for input validation
constexpr size_t MAX_BUFFER_SIZE = 1024 * 1024; // 1 MB Max buffer size

// Function to print the buffer contents
void printBuffer(const char* buffer, size_t size) {
    if (!buffer) {
        std::cerr << "Error: Buffer is null!" << std::endl;
        return;
    }

    std::cout << "Buffer contents (first 100 bytes or up to buffer size):" << std::endl;
    for (size_t i = 0; i < std::min(size, size_t(100)); ++i) {
        std::cout << static_cast<int>(buffer[i]) << " ";
    }
    std::cout << std::endl;
}

int main(int argc, char* argv[]) {
    // Input validation: Check if buffer size is provided
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <buffer_size>" << std::endl;
        return EXIT_FAILURE;
    }

    // Secure input parsing: Validate the buffer size
    size_t bufferSize = 0;
    try {
        long inputSize = std::stol(argv[1]);

        // Check if input size is within a valid range
        if (inputSize <= 0 || inputSize > std::numeric_limits<size_t>::max() || inputSize > MAX_BUFFER_SIZE) {
            throw std::invalid_argument("Invalid buffer size");
        }

        bufferSize = static_cast<size_t>(inputSize);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: Invalid buffer size argument. Must be a positive integer <= " << MAX_BUFFER_SIZE << " bytes." << std::endl;
        return EXIT_FAILURE;
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: Buffer size is too large." << std::endl;
        return EXIT_FAILURE;
    }

    // Secure memory allocation
    char* buffer = static_cast<char*>(std::malloc(bufferSize));
    if (!buffer) {
        std::cerr << "Error: Memory allocation failed." << std::endl;
        return EXIT_FAILURE;
    }

    // Initialize the buffer to zeros (secure memory handling)
    std::memset(buffer, 0, bufferSize);

    // Print buffer contents
    printBuffer(buffer, bufferSize);

    // Secure memory deallocation
    std::free(buffer);
    buffer = nullptr;

    return EXIT_SUCCESS;
}
