#include <iostream>
#include <cstring>  // for memcpy and strlen

int main() {
    const char* message = "Hello, World!";
    
    // Determine the length of the message using strlen
    size_t messageLength = strlen(message);
    
    // Allocate a buffer large enough to hold the message
    char buffer[messageLength + 1];  // +1 for the null terminator
    
    // Copy the message to the buffer using memcpy
    memcpy(buffer, message, messageLength + 1);  // Copy the message along with the null terminator
    
    // Print the buffer to verify it contains the message
    std::cout << "Buffer contains: " << buffer << std::endl;
    
    return 0;
}
