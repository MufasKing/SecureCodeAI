#include <iostream>
#include <cstring> // For memcpy
#include <cstdlib> // For malloc and free

int main() {
    // Allocate two chunks of memory, each of size 10
    char* chunk1 = (char*)malloc(10 * sizeof(char));
    char* chunk2 = (char*)malloc(10 * sizeof(char));

    // Check if memory allocation was successful
    if (chunk1 == nullptr || chunk2 == nullptr) {
        std::cerr << "Memory allocation failed" << std::endl;
        return 1;
    }

    // Initialize chunk1 with some data
    for (int i = 0; i < 10; ++i) {
        chunk1[i] = 'A' + i; // Fill with characters A to J
    }

    // Copy the contents of the first chunk into the second chunk
    memcpy(chunk2, chunk1, 10 * sizeof(char));

    // Free the first chunk
    free(chunk1);

    // Free the second chunk
    free(chunk2);

    return 0;
}