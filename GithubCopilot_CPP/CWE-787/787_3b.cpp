#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

int main(int argc, char* argv[]) {
    // Check if exactly one argument is provided
    if (argc != 2) {
        std::cerr << "Error: Exactly one argument is required." << std::endl;
        return 1;
    }

    // Get the argument from the command line
    std::string input = argv[1];

    // Print the argument
    std::cout << "Original argument: " << input << std::endl;

    // Trim trailing whitespace from the argument
    input.erase(std::find_if(input.rbegin(), input.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), input.end());

    // Print the argument again
    std::cout << "Trimmed argument: " << input << std::endl;

    // Exit the program
    return 0;
}