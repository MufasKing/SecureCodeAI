#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>

// Function to trim trailing whitespace
std::string trimTrailingWhitespace(const std::string& input) {
    std::size_t end = input.find_last_not_of(" \t\n\r");
    if (end == std::string::npos) {
        return "";  // No non-whitespace characters found
    }
    return input.substr(0, end + 1);
}

int main(int argc, char* argv[]) {
    // 1. Argument Validation
    if (argc != 2) {
        std::cerr << "Error: Exactly one argument is required." << std::endl;
        return 1; // Exit with error code
    }

    // 2. Input Retrieval
    std::string input = argv[1];

    // 3. Print the original argument
    std::cout << "Original input: \"" << input << "\"" << std::endl;

    // 4. Trim trailing whitespace
    input = trimTrailingWhitespace(input);

    // 5. Print the trimmed argument
    std::cout << "Trimmed input: \"" << input << "\"" << std::endl;

    // 6. Exit the program
    return 0;
}
