#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

// Function to trim trailing whitespace
std::string trimTrailingWhitespace(const std::string& str) {
    size_t end = str.find_last_not_of(" \t\n\r\f\v");
    return (end == std::string::npos) ? "" : str.substr(0, end + 1);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "No argument provided." << std::endl;
        return 1;
    }

    std::string input = argv[1];
    std::string trimmedInput = trimTrailingWhitespace(input);

    std::cout << "Trimmed argument: " << trimmedInput << std::endl;

    return 0;
}