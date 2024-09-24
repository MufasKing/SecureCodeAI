#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    // Check if the argument count is correct
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <buffer_size>" << std::endl;
        return 1;
    }

    // Convert the argument to an integer
    int bufferSize = std::atoi(argv[1]);
    if (bufferSize <= 0) {
        std::cerr << "Buffer size must be a positive integer." << std::endl;
        return 1;
    }

    // Allocate the buffer
    char* buffer = new char[bufferSize];

    // Fill the buffer with some data (for demonstration, we use 'A')
    for (int i = 0; i < bufferSize; ++i) {
        buffer[i] = 'A'; // Fill with 'A'
    }

    // Print the contents of the buffer
    std::cout << "Buffer contents: ";
    for (int i = 0; i < bufferSize; ++i) {
        std::cout << buffer[i];
    }
    std::cout << std::endl;

    // Clean up allocated memory
    delete[] buffer;

    return 0;
}
