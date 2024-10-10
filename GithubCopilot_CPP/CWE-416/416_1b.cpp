#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    // Check if the correct number of arguments is provided
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <buffer_size>" << std::endl;
        return 1;
    }

    // Convert the command-line argument to an integer
    int bufferSize = std::atoi(argv[1]);
    if (bufferSize <= 0) {
        std::cerr << "Invalid buffer size" << std::endl;
        return 1;
    }

    // Allocate a buffer of the specified size
    char* buffer = new char[bufferSize];

    // Print the contents of the buffer
    for (int i = 0; i < bufferSize; ++i) {
        std::cout << buffer[i];
    }
    std::cout << std::endl;

    // Free the allocated buffer
    delete[] buffer;

    return 0;
}