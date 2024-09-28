#include <iostream>
#include <cstdlib>   // For std::strtol
#include <cerrno>    // For errno
#include <climits>   // For INT_MAX and INT_MIN

int main(int argc, char *argv[]) {
    // Ensure at least one argument is passed (the program name is counted as an argument)
    if (argc != 2) {
        std::cerr << "Error: Please provide exactly one integer argument." << std::endl;
        return 1;
    }

    char *endptr = nullptr;
    errno = 0;  // Reset errno before calling strtol

    // Attempt to convert the input string to a long integer
    long value = std::strtol(argv[1], &endptr, 10);

    // Check for conversion errors
    if (errno == ERANGE || value > INT_MAX || value < INT_MIN) {
        std::cerr << "Error: The value is out of range." << std::endl;
        return 1;
    }

    if (endptr == argv[1] || *endptr != '\0') {
        std::cerr << "Error: Invalid input. Please enter a valid integer." << std::endl;
        return 1;
    }

    // Now that the input is validated, we can safely add 1000 to it
    int result = static_cast<int>(value) + 1000;

    // Output the result
    std::cout << "Result: " << result << std::endl;

    return 0;
}
