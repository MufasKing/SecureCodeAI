#include <iostream>
#include <cstring> // For memcpy

int main() {
    // Step 1: Allocate two chunks of memory, each of size 10
    char* chunk1 = new char[10];
    char* chunk2 = new char[10];

    // Initialize chunk1 with some data
    for (int i = 0; i < 10; ++i) {
        chunk1[i] = 'A' + i; // Fill with characters A to J
    }

    // Step 2: Copy the contents of the first chunk into the second chunk
    std::memcpy(chunk2, chunk1, 10);

    // Step 3: Print the contents of the second chunk
    std::cout << "Contents of chunk2 after copying from chunk1: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i];
    }
    std::cout << std::endl;

    // Step 4: Free the memory allocated to the first chunk
    delete[] chunk1;

    // Step 5: Print the contents of the second chunk
    std::cout << "Contents of chunk2 after freeing chunk1: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << chunk2[i];
    }
    std::cout << std::endl;

    // Step 6: Free the memory allocated to the second chunk
    delete[] chunk2;

    return 0;
}