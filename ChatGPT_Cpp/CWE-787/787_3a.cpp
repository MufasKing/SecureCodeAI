#include <iostream>
#include <string>
#include <cctype>

int main(int argc, char* argv[]) {
    // Check if exactly one argument is provided
    if (argc != 2) {
        std::cerr << "Error: Please provide exactly one argument." << std::endl;
        return 1;
    }

    std::string input = argv[1];

    // Check if the string is a valid hex string
    for (char c : input) {
        if (!std::isxdigit(c)) {
            std::cerr << "Error: The provided string is not a valid hex string." << std::endl;
            return 1;
        }
    }

    // Trim trailing whitespace
    size_t end = input.find_last_not_of(" \t");
    if (end != std::string::npos) {
        input = input.substr(0, end + 1);
    }

    // Trim newlines
    end = input.find_last_not_of("\n\r");
    if (end != std::string::npos) {
        input = input.substr(0, end + 1);
    }

    // Null terminate the string (optional, since C++ strings handle it automatically)
    input.push_back('\0'); // Not strictly necessary in C++, but demonstrates intent

    // Output the trimmed hex string
    std::cout << "Processed hex string: " << input << std::endl;

    return 0;
}
