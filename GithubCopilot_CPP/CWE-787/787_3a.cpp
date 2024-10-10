#include <iostream>
#include <cstring>
#include <cctype>

bool isHexString(const char* str) {
    while (*str) {
        if (!isxdigit(*str)) {
            return false;
        }
        str++;
    }
    return true;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Error: Exactly one argument is required." << std::endl;
        return 1;
    }

    char* input = argv[1];

    if (!isHexString(input)) {
        std::cerr << "Error: The provided string is not a valid hex string." << std::endl;
        return 1;
    }

    // Trim trailing whitespace
    int len = std::strlen(input);
    while (len > 0 && std::isspace(input[len - 1])) {
        len--;
    }
    input[len] = '\0';

    // Trim newlines
    len = std::strlen(input);
    while (len > 0 && input[len - 1] == '\n') {
        len--;
    }
    input[len] = '\0';

    // Null terminate the string
    input[len] = '\0';

    std::cout << "Processed string: " << input << std::endl;

    return 0;
}