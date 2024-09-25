#include <iostream>
#include <cstdlib>
#include <string>

int runCommand(const std::string& username) {
    std::string command = "id " + username;
    int exitStatus = system(command.c_str());
    return exitStatus;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return 1;
    }

    std::string username = argv[1];
    int status = runCommand(username);

    std::cout << "Exit status: " << status << std::endl;

    return status;
}