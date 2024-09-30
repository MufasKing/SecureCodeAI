#include <iostream>
#include <stdexcept>

void allocateAndFreeBuffer(size_t buffer_size, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        // Allocate memory
        int* buffer = nullptr;
        try {
            buffer = new int[buffer_size];
        } catch (const std::bad_alloc& e) {
            std::cerr << "Memory allocation failed: " << e.what() << std::endl;
            return;
        }

        // Initialize memory
        for (size_t j = 0; j < buffer_size; ++j) {
            buffer[j] = static_cast<int>(j);
        }

        // Perform operations on buffer (if any)
        // ...

        // Free memory
        delete[] buffer;
        buffer = nullptr;
    }
}

int main() {
    size_t buffer_size = 100;
    int iterations = 10;

    allocateAndFreeBuffer(buffer_size, iterations);

    return 0;
}