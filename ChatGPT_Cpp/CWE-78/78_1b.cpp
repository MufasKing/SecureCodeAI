#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

void executeCommand(const std::string& command) {
    // Open the command for reading.
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Failed to run command.\n";
        exit(1);
    }

    // Buffer to store the output of the command.
    char buffer[128];

    // Read the output and print to the console.
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        std::cout << buffer;
    }

    // Close the pipe.
    pclose(pipe);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>\n";
        return 1;
    }

    // Retrieve the username from command-line arguments.
    std::string username = argv[1];

    // Create the command: cat /etc/passwd | grep <username>
    std::string command = "cat /etc/passwd | grep " + username;

    // Execute the command.
    executeCommand(command);

    return 0;
}
