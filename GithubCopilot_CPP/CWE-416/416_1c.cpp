#include <iostream>

int main() {
    const int buffer_size = 1024; // Define the buffer size
    char* buffer = new char[buffer_size]; // Allocate memory for the buffer

    // Loop to free the buffer
    for (int i = 0; i < 1; ++i) {
        delete[] buffer; // Free the buffer
        buffer = nullptr; // Set the pointer to nullptr to avoid dangling pointer
    }

    return 0;
}