#include <iostream>
#include <string>
#include <cstdarg>
#include <vector>
#include <sstream>

// Function to execute a command line utility
void executeCommand(const std::string& command) {
    system(command.c_str());
}

// Function to create a formatted string
std::string print(const char* format, ...) {
    va_list args;
    va_start(args, format);
    
    // Estimate the size of the formatted string
    size_t size = vsnprintf(nullptr, 0, format, args) + 1;
    std::vector<char> buffer(size);
    
    // Format the string
    vsnprintf(buffer.data(), size, format, args);
    va_end(args);
    
    return std::string(buffer.data(), buffer.size() - 1);
}

int main() {
    // Create the command string using the print function
    std::string command = print("ls %s", "-l");
    
    // Execute the command
    executeCommand(command);
    
    return 0;
}