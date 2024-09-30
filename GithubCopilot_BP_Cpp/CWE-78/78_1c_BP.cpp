#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>
#include <sys/wait.h>

// Function to run the command and return the exit status
int runCommand(const std::string& username) {
    std::string command = "id " + username;
    int status = system(command.c_str());
    return WEXITSTATUS(status);
}

// Function to validate the username
bool isValidUsername(const std::string& username) {
    // Username should only contain alphanumeric characters and underscores
    std::regex usernameRegex("^[a-zA-Z0-9_]+$");
    return std::regex_match(username, usernameRegex);
}

int main(int argc, char* argv[]) {
    // Validate the number of arguments
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return 1;
    }

    std::string username = argv[1];

    // Validate the username input
    if (!isValidUsername(username)) {
        std::cerr << "Invalid username. Only alphanumeric characters and underscores are allowed." << std::endl;
        return 1;
    }

    // Run the command and get the exit status
    int exitStatus = runCommand(username);

    // Print the exit status
    std::cout << "Exit status: " << exitStatus << std::endl;

    return exitStatus;
}