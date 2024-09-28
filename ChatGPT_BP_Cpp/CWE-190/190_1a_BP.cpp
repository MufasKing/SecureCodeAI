#include <iostream>
#include <stdexcept>
#include <climits> // for INT_MAX, INT_MIN
#include <cstdlib> // for strtol
#include <cerrno>  // for errno

// Function to safely convert string to integer
long safeStringToInt(const char* str) {
    char* end;
    errno = 0; // reset errno before the conversion
    long value = std::strtol(str, &end, 10);

    // Check for conversion errors
    if (errno == ERANGE || value > INT_MAX || value < INT_MIN) {
        throw std::out_of_range("Integer overflow or underflow");
    }
    if (*end != '\0') {
        throw std::invalid_argument("Invalid input: Not a valid integer");
    }

    return value;
}

// Function to safely add 1000 and check for overflow/underflow
int safeAdd(int value, int to_add) {
    if (value > 0 && to_add > INT_MAX - value) {
        throw std::overflow_error("Integer overflow");
    }
    if (value < 0 && to_add < INT_MIN - value) {
        throw std::underflow_error("Integer underflow");
    }
    return value + to_add;
}

// Main function
int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <integer>" << std::endl;
        return 1;
    }

    try {
        // Convert input string to integer safely
        int value = static_cast<int>(safeStringToInt(argv[1]));

        // Add 1000 safely, checking for overflow/underflow
        int result = safeAdd(value, 1000);

        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        // Catch any exceptions and display error message
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
