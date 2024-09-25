#include <iostream>
#include <cstring>  // for memcpy and strlen

int main() {
    const char* source = "Hello";  // source string
    size_t length = strlen(source);  // get the length of the source string

    // Create a buffer to hold the copied string, plus 1 for the null terminator
    char buffer[length + 1];

    // Use memcpy to copy the string from source to buffer
    memcpy(buffer, source, length + 1);  // +1 to include the null terminator

    // Print the copied string
    std::cout << "Copied string: " << buffer << std::endl;

    return 0;
}
