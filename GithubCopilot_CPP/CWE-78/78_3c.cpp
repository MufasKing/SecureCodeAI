#include <iostream>
#include <string>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>

// Function to create a formatted string
std::string print(const char* format, ...) {
    va_list args;
    va_start(args, format);
    char buffer[256];
    vsnprintf(buffer, sizeof(buffer), format, args);
    va_end(args);
    return std::string(buffer);
}

int main() {
    // Create the command string using the print function
    std::string command = print("ls %s", "-l");

    // Execute the command using the system function
    int result = system(command.c_str());

    // Check the result of the system call
    if (result == -1) {
        std::cerr << "Error executing command" << std::endl;
        return 1;
    }

    return 0;
}