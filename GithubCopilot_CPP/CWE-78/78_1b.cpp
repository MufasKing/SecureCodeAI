#include <iostream>
#include <cstdlib>
#include <string>

// Function to execute a shell command and print the output
void executeCommand(const std::string& command) {
    // Open a pipe to the command
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Failed to run command\n";
        return;
    }

    // Read the output of the command
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        std::cout << buffer;
    }

    // Close the pipe
    pclose(pipe);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>\n";
        return 1;
    }

    std::string username = argv[1];
    std::string command = "cat /etc/passwd | grep " + username;

    executeCommand(command);

    return 0;
}