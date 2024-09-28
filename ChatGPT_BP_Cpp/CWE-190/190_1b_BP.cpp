#include <iostream>
#include <limits>
#include <cstdlib>
#include <cerrno>
#include <climits>

const int OFFSET = 1000;

bool isInteger(const char* str, int& outValue) {
    char* end;
    errno = 0; // Reset errno before calling strtol
    long value = std::strtol(str, &end, 10);

    // Check for conversion errors
    if (errno == ERANGE || value < INT_MIN || value > INT_MAX) {
        return false;
    }

    // Ensure entire string was converted and no extra characters exist
    if (*end != '\0') {
        return false;
    }

    outValue = static_cast<int>(value);
    return true;
}

bool willAdditionOverflow(int a, int b) {
    if (b > 0 && a > INT_MAX - b) {
        return true; // Overflow
    }
    if (b < 0 && a < INT_MIN - b) {
        return true; // Underflow
    }
    return false;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <integer>\n";
        return EXIT_FAILURE;
    }

    int inputValue;
    if (!isInteger(argv[1], inputValue)) {
        std::cerr << "Error: Invalid input. Please enter a valid integer.\n";
        return EXIT_FAILURE;
    }

    // Check for overflow/underflow when adding OFFSET
    if (willAdditionOverflow(inputValue, OFFSET)) {
        std::cerr << "Error: Addition of " << OFFSET << " would result in overflow or underflow.\n";
        return EXIT_FAILURE;
    }

    int result = inputValue + OFFSET;

    std::cout << "Result: " << result << std::endl;
    return EXIT_SUCCESS;
}
