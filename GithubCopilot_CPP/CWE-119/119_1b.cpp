#include <iostream>
#include <cstring>

int main() {
    // Source message
    const char* message = "Hello, World!";
    
    // Buffer to hold the copied message
    char buffer[50];
    
    // Copy the message to the buffer
    std::memcpy(buffer, message, std::strlen(message) + 1); // +1 to include the null terminator
    
    // Print the buffer to verify the copy
    std::cout << "Buffer contains: " << buffer << std::endl;
    
    return 0;
}