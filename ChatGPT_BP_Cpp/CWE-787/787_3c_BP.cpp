#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>   // for isspace
#include <stdexcept> // for std::runtime_error

// Function to validate input: ensures that there is one command line argument
void validateInput(int argc) {
    if (argc != 2) {
        throw std::invalid_argument("Error: Please provide exactly one argument.");
    }
}

// Function to sanitize input: Ensures that the input is free of unsafe characters
std::string sanitizeInput(const std::string& input) {
    // Example sanitization: remove control characters
    std::string sanitized;
    sanitized.reserve(input.size());
    
    for (char c : input) {
        if (std::isprint(c) || std::isspace(c)) {
            sanitized.push_back(c); // Only allow printable and whitespace characters
        } else {
            throw std::runtime_error("Error: Input contains invalid or non-printable characters.");
        }
    }

    return sanitized;
}

// Function to trim trailing whitespace from the input string
std::string trimWhitespace(const std::string& input) {
    size_t end = input.find_last_not_of(" \t\n\r\f\v");
    return (end == std::string::npos) ? "" : input.substr(0, end + 1);
}

// Function to encode output to avoid any potential output injection
std::string encodeOutput(const std::string& input) {
    std::string encoded;
    encoded.reserve(input.size());

    for (char c : input) {
        switch (c) {
            case '<':
                encoded += "&lt;";
                break;
            case '>':
                encoded += "&gt;";
                break;
            case '&':
                encoded += "&amp;";
                break;
            case '\"':
                encoded += "&quot;";
                break;
            case '\'':
                encoded += "&#39;";
                break;
            default:
                encoded += c;
        }
    }

    return encoded;
}

// Function to securely clear sensitive data from memory
void secureClear(std::string& sensitiveData) {
    std::fill(sensitiveData.begin(), sensitiveData.end(), '\0'); // Overwrite with null characters
    sensitiveData.clear(); // Clear the string content
}

// Main function
int main(int argc, char* argv[]) {
    try {
        // Step 1: Input Validation
        validateInput(argc);

        // Step 2: Input Sanitization
        std::string argument = sanitizeInput(argv[1]);

        // Step 3: Whitespace Trimming
        argument = trimWhitespace(argument);

        // Step 4: Output Encoding
        std::string safeOutput = encodeOutput(argument);

        // Step 5: Output the sanitized and trimmed argument
        std::cout << "Processed Argument: " << safeOutput << std::endl;

        // Step 6: Securely clear the sensitive data from memory
        secureClear(argument);
        secureClear(safeOutput);
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
