#include <iostream>
#include <cstdlib>
#include <cstring>

void executeCommand(const char* command) {
    int result = system(command);
    if (result == -1) {
        std::cerr << "Error executing command." << std::endl;
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char* argv[]) {
    // Input Validation
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return EXIT_FAILURE;
    }

    const char* username = argv[1];
    const char* baseCommand = "cat /etc/passwd | grep ";
    
    // Dynamic Memory Allocation for command string
    size_t commandLength = strlen(baseCommand) + strlen(username) + 1;
    char* command = new(std::nothrow) char[commandLength];
    if (!command) {
        std::cerr << "Memory allocation failed." << std::endl;
        return EXIT_FAILURE;
    }

    // Command Construction
    strcpy(command, baseCommand);
    strcat(command, username);

    // Command Execution
    executeCommand(command);

    // Free allocated memory
    delete[] command;

    return EXIT_SUCCESS;
}