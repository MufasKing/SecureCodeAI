#include <iostream>
#include <climits>
#include <cstdlib>
#include <cerrno>

int main(int argc, char *argv[]) {
    // Check if the correct number of arguments is passed
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    // Initialize variables for conversion
    char *endptr;
    errno = 0; // To distinguish success/failure after call

    // Convert string to long
    long val = strtol(argv[1], &endptr, 10);

    // Check for various possible errors
    if ((errno == ERANGE && (val == LONG_MAX || val == LONG_MIN)) || (errno != 0 && val == 0)) {
        perror("strtol");
        return 1;
    }

    if (endptr == argv[1]) {
        std::cerr << "No digits were found in the input." << std::endl;
        return 1;
    }

    // Check for integer overflow/underflow
    if (val > INT_MAX || val < INT_MIN) {
        std::cerr << "Integer overflow or underflow occurred." << std::endl;
        return 1;
    }

    // Successful conversion
    int result = static_cast<int>(val);
    std::cout << "Converted integer: " << result << std::endl;

    return 0;
}