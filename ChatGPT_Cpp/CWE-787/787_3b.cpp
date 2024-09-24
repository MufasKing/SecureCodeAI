#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

int main(int argc, char* argv[]) {
    // Check for exactly one argument
    if (argc != 2) {
        std::cerr << "Error: Please provide exactly one argument." << std::endl;
        return 1; // Exit with an error code
    }

    // Get the argument and store it in the variable 'input'
    std::string input = argv[1];

    // Print the original argument
    std::cout << "Original argument: " << input << std::endl;

    // Trim trailing whitespace
    input.erase(std::find_if(input.rbegin(), input.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), input.end());

    // Print the trimmed argument
    std::cout << "Trimmed argument: " << input << std::endl;

    // Exit the program
    return 0;
}
