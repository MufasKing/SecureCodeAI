#include <iostream>
#include <cstring>

int main() {
    // Allocate two chunks of memory, each of size 10
    char* chunk1 = new char[10];
    char* chunk2 = new char[10];

    // Initialize the first chunk with some values
    for (int i = 0; i < 10; ++i) {
        chunk1[i] = 'A' + i; // Fill with characters A to J
    }

    // Copy the contents of the first chunk into the second chunk
    std::memcpy(chunk2, chunk1, 10);

    // Print the contents of the second chunk
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i] << ' ';
    }
    std::cout << std::endl;

    // Free the allocated memory
    delete[] chunk1;
    delete[] chunk2;

    return 0;
}