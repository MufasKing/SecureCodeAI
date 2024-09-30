#include <iostream>
#include <cstring> // for memcpy_s
#include <cstdlib> // for malloc and free

int main() {
    // Allocate two chunks of memory, each of size 10
    size_t size = 10;
    char* chunk1 = (char*)malloc(size);
    char* chunk2 = (char*)malloc(size);

    // Error handling for memory allocation
    if (chunk1 == nullptr || chunk2 == nullptr) {
        std::cerr << "Memory allocation failed" << std::endl;
        if (chunk1) free(chunk1);
        if (chunk2) free(chunk2);
        return 1;
    }

    // Initialize the first chunk with some values
    for (size_t i = 0; i < size; ++i) {
        chunk1[i] = 'A' + i; // Example initialization
    }

    // Copy the contents of the first chunk into the second chunk
    errno_t err = memcpy_s(chunk2, size, chunk1, size);
    if (err != 0) {
        std::cerr << "Memory copy failed" << std::endl;
        free(chunk1);
        free(chunk2);
        return 1;
    }

    // Free the first chunk
    free(chunk1);

    // Free the second chunk
    free(chunk2);

    return 0;
}