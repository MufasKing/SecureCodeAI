#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/wait.h>
#include <limits>

bool isValidUsername(const std::string& username) {
    // A valid username must not be empty and should contain only valid characters
    if (username.empty() || username.length() > 32) return false; // Example length limit
    for (char c : username) {
        if (!(isalnum(c) || c == '_' || c == '-')) return false; // Only alphanumeric, underscore, and dash allowed
    }
    return true;
}

int runIdCommand(const std::string& username) {
    pid_t pid = fork(); // Create a child process
    if (pid < 0) {
        std::cerr << "Fork failed." << std::endl;
        return -1; // Return -1 for fork failure
    } else if (pid == 0) { // Child process
        // Prepare the command
        const char* cmd = "id";
        const char* args[] = {cmd, username.c_str(), nullptr};

        // Execute the command
        execvp(cmd, const_cast<char* const*>(args));

        // If execvp fails
        std::cerr << "Failed to execute command." << std::endl;
        exit(EXIT_FAILURE); // Exit child process with failure
    } else { // Parent process
        int status;
        waitpid(pid, &status, 0); // Wait for the child process to finish
        return WEXITSTATUS(status); // Return the exit status of the command
    }
}

int main(int argc, char* argv[]) {
    // Check command-line argument count
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return EXIT_FAILURE;
    }

    std::string username = argv[1];

    // Validate the username input
    if (!isValidUsername(username)) {
        std::cerr << "Invalid username provided. Please use alphanumeric characters, '_', or '-' only." << std::endl;
        return EXIT_FAILURE;
    }

    // Run the id command and get the exit status
    int exitStatus = runIdCommand(username);

    // Check for execution errors
    if (exitStatus == -1) {
        std::cerr << "Error occurred while executing the command." << std::endl;
        return EXIT_FAILURE;
    }

    // Print the exit status of the command
    std::cout << "The exit status of the command 'id " << username << "' is: " << exitStatus << std::endl;

    return EXIT_SUCCESS;
}
