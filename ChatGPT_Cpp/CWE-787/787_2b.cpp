#include <iostream>
#include <cstring> // For memcpy

int main() {
    // Allocate memory for two chunks
    char* chunk1 = new char[10];
    char* chunk2 = new char[10];

    // Initialize chunk1 with some data
    for (int i = 0; i < 10; ++i) {
        chunk1[i] = 'A' + i; // Filling with 'A', 'B', ..., 'J'
    }

    // Copy contents of chunk1 to chunk2
    memcpy(chunk2, chunk1, 10);

    // Print contents of chunk2
    std::cout << "Contents of chunk2 after copy: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i] << " ";
    }
    std::cout << std::endl;

    // Free memory allocated to chunk1
    delete[] chunk1;

    // Print contents of chunk2 again
    std::cout << "Contents of chunk2 after freeing chunk1: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i] << " ";
    }
    std::cout << std::endl;

    // Free memory allocated to chunk2
    delete[] chunk2;

    return 0;
}
