#include <iostream>
#include <cstring>    // For strlen, strcmp
#include <cctype>     // For isspace
#include <stdexcept>  // For std::invalid_argument

int main(int argc, char* argv[]) {
    try {
        // Step 1: Validate input arguments (ensure exactly one argument is passed)
        if (argc != 2) {
            throw std::invalid_argument("Error: You must provide exactly one argument.");
        }

        // Step 2: Check if the argument is a valid string
        char* input = argv[1];
        if (input == nullptr || strlen(input) == 0) {
            throw std::invalid_argument("Error: The provided argument is not a valid string.");
        }

        // Step 3: Trim trailing whitespace characters (spaces, tabs)
        int length = strlen(input);
        int end = length - 1;
        
        // Trim trailing spaces and tabs
        while (end >= 0 && std::isspace(input[end])) {
            --end;
        }

        // If there's any trailing whitespace, update the string length
        if (end < length - 1) {
            input[end + 1] = '\0';
        }

        // Step 4: Trim newlines ('\n', '\r')
        length = strlen(input);  // recalculate length after trimming
        end = length - 1;
        while (end >= 0 && (input[end] == '\n' || input[end] == '\r')) {
            --end;
        }

        // If there's any trailing newline, update the string length
        if (end < length - 1) {
            input[end + 1] = '\0';
        }

        // Step 5: Ensure the string is null-terminated (done implicitly above)

        // Output the final processed string
        std::cout << "Processed String: \"" << input << "\"" << std::endl;

    } catch (const std::exception& ex) {
        // Handle errors and output error message
        std::cerr << ex.what() << std::endl;
        return 1;  // Return non-zero status code for failure
    }

    return 0;  // Return zero status code for success
}
