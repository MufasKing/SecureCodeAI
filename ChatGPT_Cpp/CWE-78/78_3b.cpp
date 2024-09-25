#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstdarg>

// Function to execute a command
void executeCommand(const std::string& command) {
    // Use system() to execute the command
    int result = system(command.c_str());
    if (result == -1) {
        std::cerr << "Error executing command: " << command << std::endl;
    }
}

// Variadic template to create a formatted command string
template<typename... Args>
std::string print(const std::string& format, Args... args) {
    size_t size = std::snprintf(nullptr, 0, format.c_str(), args...) + 1; // Extra space for '\0'
    std::unique_ptr<char[]> buf(new char[size]); // Create a buffer
    std::snprintf(buf.get(), size, format.c_str(), args...); // Format the string
    return std::string(buf.get(), buf.get() + size - 1); // Convert to string
}

int main() {
    // Create the command string using print
    std::string command = print("ls %s", "-l"); // Example command with '-l' option
    // Execute the command
    executeCommand(command);
    return 0;
}
