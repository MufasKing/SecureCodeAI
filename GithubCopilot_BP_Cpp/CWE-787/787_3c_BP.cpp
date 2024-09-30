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
    // Validate input
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <string>" << std::endl;
        return 1;
    }

    // Secure string handling
    std::string input(argv[1]);

    // Trim trailing whitespace
    std::string trimmedInput = trimTrailingWhitespace(input);

    // Print the trimmed argument
    std::cout << "Trimmed input: " << trimmedInput << std::endl;

    return 0;
}