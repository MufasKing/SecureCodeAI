#include <iostream>
#include <cstdlib>
#include <string>

int runCommand(const std::string& username) {
    // Construct the command string
    std::string command = "id " + username;

    // Use system to execute the command
    int exitStatus = system(command.c_str());

    // Return the exit status (WIFEXITED is used to get the exit code)
    return WIFEXITED(exitStatus) ? WEXITSTATUS(exitStatus) : -1;
}

int main(int argc, char* argv[]) {
    // Check if the username is provided as a command line argument
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return 1; // Exit with error if no username is provided
    }

    std::string username = argv[1];

    // Run the command and get the exit status
    int status = runCommand(username);

    // Print the exit status
    std::cout << "Exit status of command 'id " << username << "': " << status << std::endl;

    return 0;
}
