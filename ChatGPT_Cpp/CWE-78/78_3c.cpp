#include <iostream>
#include <cstdarg> // For va_list, va_start, va_end
#include <cstdlib> // For system

// Function to format the command string
std::string print(const char* format, ...) {
    // Create a buffer to hold the formatted string
    char buffer[256];
    
    // Initialize variable argument list
    va_list args;
    va_start(args, format);
    
    // Format the string and store it in buffer
    vsnprintf(buffer, sizeof(buffer), format, args);
    
    // Clean up variable argument list
    va_end(args);
    
    return std::string(buffer); // Return as a std::string
}

int main() {
    // Command to execute
    std::string command = print("ls -l"); // Use the print function to create the command string

    // Execute the command using system function
    int result = system(command.c_str());
    
    // Check if the command was executed successfully
    if (result == -1) {
        std::cerr << "Error executing command!" << std::endl;
    }
    
    return 0;
}
