#include <iostream>

int main() {
    const size_t buffer_size = 1024; // Size of the buffer (e.g., 1024 bytes)
    
    // Allocate the buffer
    char* buffer = new char[buffer_size];
    
    // Check if allocation was successful
    if (buffer == nullptr) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return 1; // Exit with an error code
    }

    // Free the buffer in a loop
    for (int i = 0; i < 5; ++i) { // Loop for demonstration (5 times)
        std::cout << "Freeing buffer iteration: " << i + 1 << std::endl;
        delete[] buffer; // Free the allocated buffer
        // Optionally, reallocate the buffer again
        buffer = new char[buffer_size];
        
        // Check if reallocation was successful
        if (buffer == nullptr) {
            std::cerr << "Memory allocation failed on iteration " << i + 1 << std::endl;
            return 1; // Exit with an error code
        }
    }

    // Free the buffer one last time before exiting
    delete[] buffer;

    std::cout << "Buffer freed successfully." << std::endl;
    return 0;
}
