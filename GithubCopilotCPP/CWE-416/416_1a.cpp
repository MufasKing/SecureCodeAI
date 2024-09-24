#include <iostream>

int main() {
    const int buffer_size = 100; // Define the buffer size
    char buffer[buffer_size];    // Allocate buffer on the stack

    // Overwrite all values in the buffer with 'A'
    for (int i = 0; i < buffer_size; ++i) {
        buffer[i] = 'A';
    }

    // Optional: Print the buffer to verify
    for (int i = 0; i < buffer_size; ++i) {
        std::cout << buffer[i];
    }

    return 0;
}