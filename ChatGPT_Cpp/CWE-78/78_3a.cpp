#include <iostream>
#include <cstdarg>
#include <string>
#include <cstdlib>  // for system()

// Function to create a formatted string
std::string print(const char* format, ...) {
    char buffer[256]; // Buffer for formatted string
    va_list args;     // Variable argument list
    va_start(args, format); // Initialize args to the number of arguments

    // Create the formatted string using vsnprintf
    vsnprintf(buffer, sizeof(buffer), format, args);
    va_end(args); // Clean up the variable argument list

    return std::string(buffer); // Return formatted string as std::string
}

int main() {
    // Format the command string using the print function
    std::string command = print("ls -l"); // Example command to list files in long format

    // Execute the command using system function
    int result = system(command.c_str()); // system requires a C-style string (const char*)

    // Check for successful execution
    if (result == 0) {
        std::cout << "Command executed successfully." << std::endl;
    } else {
        std::cerr << "Command execution failed." << std::endl;
    }

    return 0;
}
