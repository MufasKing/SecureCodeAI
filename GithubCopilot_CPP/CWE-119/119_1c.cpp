#include <cstring>
#include <iostream>

int main() {
    const char* source = "Hello";
    char buffer[6]; // Allocate enough space for "Hello" and the null terminator

    // Copy the string "Hello" to the buffer
    std::memcpy(buffer, source, std::strlen(source) + 1); // +1 to include the null terminator

    // Output the copied string
    std::cout << "Buffer contains: " << buffer << std::endl;

    return 0;
}