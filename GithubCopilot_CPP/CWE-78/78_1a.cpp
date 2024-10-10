#include <iostream>
#include <cstdio>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

int main() {
    const std::string username = "<username>"; // Replace <username> with the actual username
    const std::string command = "getent passwd " + username;
    std::array<char, 128> buffer;
    std::string result;

    // Open the command for reading
    std::unique_ptr<FILE, decltype(&pclose)> output(popen(command.c_str(), "r"), pclose);
    if (!output) {
        std::cerr << "popen() failed!" << std::endl;
        return 1;
    }

    // Read the output a line at a time - output it
    while (fgets(buffer.data(), buffer.size(), output.get()) != nullptr) {
        result += buffer.data();
    }

    std::cout << "User information: " << result << std::endl;

    return 0;
}