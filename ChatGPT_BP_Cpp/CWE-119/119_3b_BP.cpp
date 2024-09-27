#include <iostream>
#include <cstdlib>      // for atoi
#include <string>       // for std::string
#include <limits>       // for std::numeric_limits
#include <cerrno>       // for errno
#include <cstring>      // for strerror
#include <climits>      // for INT_MAX and INT_MIN

// Function to convert a string to an integer with robust error handling
bool convertStringToInt(const char* str, int& result) {
    char* endPtr;
    errno = 0; // Reset errno before calling strtol()

    long tempResult = strtol(str, &endPtr, 10); // Using strtol for better error checking

    // Check for errors:
    // 1. If no digits were found (endPtr points to the start of the string)
    if (endPtr == str) {
        std::cerr << "Error: No digits found in argument \"" << str << "\".\n";
        return false;
    }

    // 2. If there are any non-numeric characters in the string
    if (*endPtr != '\0') {
        std::cerr << "Error: Argument \"" << str << "\" contains non-numeric characters.\n";
        return false;
    }

    // 3. Check for out-of-range values
    if ((errno == ERANGE && (tempResult == LONG_MAX || tempResult == LONG_MIN)) || tempResult > INT_MAX || tempResult < INT_MIN) {
        std::cerr << "Error: Argument \"" << str << "\" is out of the range for an int.\n";
        return false;
    }

    // Assign the valid converted value
    result = static_cast<int>(tempResult);
    return true;
}

int main(int argc, char* argv[]) {
    // Check if there are enough arguments passed
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <list of integers>\n";
        return 1; // Return with error code 1 for insufficient arguments
    }

    // Process each argument passed, starting from argv[1] as argv[0] is the program name
    for (int i = 1; i < argc; ++i) {
        int convertedValue;
        if (convertStringToInt(argv[i], convertedValue)) {
            std::cout << "Argument " << i << " (" << argv[i] << ") converted to integer: " << convertedValue << "\n";
        } else {
            std::cerr << "Error converting argument " << i << ": \"" << argv[i] << "\" to an integer.\n";
            return 2; // Exit with error code 2 for conversion errors
        }
    }

    return 0; // Program executed successfully
}
