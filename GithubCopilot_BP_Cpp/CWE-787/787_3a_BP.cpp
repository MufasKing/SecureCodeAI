#include <iostream>
#include <cstring>

int main(int argc, char* argv[]) {
    // Argument Validation
    if (argc != 2) {
        std::cerr << "Error: Exactly one argument is required." << std::endl;
        return 1;
    }

    // Input Validation
    char* input = argv[1];
    if (!input) {
        std::cerr << "Error: Argument is not a valid string." << std::endl;
        return 1;
    }

    // Whitespace Trimming
    int len = std::strlen(input);
    while (len > 0 && std::isspace(input[len - 1])) {
        input[--len] = '\0';
    }

    // Newline Trimming
    for (int i = 0; i < len; ++i) {
        if (input[i] == '\n') {
            input[i] = '\0';
            break;
        }
    }

    // Null Termination
    input[len] = '\0';

    std::cout << "Processed string: " << input << std::endl;
    return 0;
}