#include <iostream>
#include <cstring> // For memcpy

int main() {
    // Allocate two chunks of memory, each of size 10 bytes
    char* chunk1 = new char[10];
    char* chunk2 = new char[10];

    // Initialize chunk1 with some data
    for (int i = 0; i < 10; ++i) {
        chunk1[i] = 'A' + i; // Fill with letters A-J
    }

    // Copy contents from chunk1 to chunk2
    std::memcpy(chunk2, chunk1, 10);

    // Print contents of both chunks
    std::cout << "Contents of chunk1: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk1[i] << ' ';
    }
    std::cout << std::endl;

    std::cout << "Contents of chunk2: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i] << ' ';
    }
    std::cout << std::endl;

    // Free the first chunk
    delete[] chunk1;

    // Free the second chunk
    delete[] chunk2;

    return 0;
}
