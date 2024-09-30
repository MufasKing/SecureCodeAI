#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

void logError(const std::string& message) {
    std::ofstream logFile("error.log", std::ios_base::app);
    logFile << message << std::endl;
    logFile.close();
}

bool isValidUsername(const std::string& username) {
    // Check if the username is non-empty and contains only valid characters
    if (username.empty() || username.length() > 32) {
        return false;
    }
    return std::all_of(username.begin(), username.end(), [](char c) {
        return std::isalnum(c) || c == '.' || c == '_' || c == '-';
    });
}

void executeCommand(const std::string& command) {
    // Use popen for command execution to avoid shell injection
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        logError("Failed to open pipe for command: " + command);
        std::cerr << "Failed to execute command." << std::endl;
        return;
    }

    char buffer[128];
    std::string result;

    // Read the output of the command
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        result += buffer;
    }

    pclose(pipe);
    std::cout << result << std::endl;  // Output the result securely
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return 1;
    }

    std::string username = argv[1];

    // Validate the username
    if (!isValidUsername(username)) {
        logError("Invalid username: " + username);
        std::cerr << "Error: Invalid username." << std::endl;
        return 1;
    }

    // Construct the command securely
    std::string command = "grep '^" + username + ":' /etc/passwd";
    
    // Execute the command
    executeCommand(command);

    return 0;
}
