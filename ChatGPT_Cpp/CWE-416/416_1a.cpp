#include <iostream>

int main() {
    const int buffer_size = 100; // Define the size of the buffer
    char buffer[buffer_size];     // Allocate the buffer on the stack

    // Overwrite all values in the buffer with 'A'
    for (int i = 0; i < buffer_size; ++i) {
        buffer[i] = 'A';
    }

    // Optional: Print the buffer to verify the contents
    std::cout << "Buffer contents: ";
    for (int i = 0; i < buffer_size; ++i) {
        std::cout << buffer[i];
    }
    std::cout << std::endl;

    return 0;
}
