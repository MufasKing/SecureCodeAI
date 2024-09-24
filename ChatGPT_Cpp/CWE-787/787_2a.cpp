#include <iostream>
#include <cstring> // For memcpy

int main() {
    // Allocate two chunks of memory, each of size 10
    const size_t size = 10;
    char* chunk1 = new char[size];
    char* chunk2 = new char[size];

    // Initialize the first chunk with some data
    for (size_t i = 0; i < size; ++i) {
        chunk1[i] = 'A' + i; // Fill with letters A-J
    }

    // Copy contents of the first chunk into the second chunk
    std::memcpy(chunk2, chunk1, size);

    // Print the contents of the second chunk
    std::cout << "Contents of the second chunk: ";
    for (size_t i = 0; i < size; ++i) {
        std::cout << chunk2[i] << " ";
    }
    std::cout << std::endl;

    // Deallocate the memory
    delete[] chunk1;
    delete[] chunk2;

    return 0;
}
