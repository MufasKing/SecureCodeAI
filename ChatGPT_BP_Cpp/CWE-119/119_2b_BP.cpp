#include <iostream>
#include <string>
#include <stdexcept>
#include <limits> // for std::numeric_limits

// Function to convert a string to an integer securely
int convertToInt(const std::string& input) {
    try {
        size_t pos;
        // Convert the string to an integer using std::stoi
        int number = std::stoi(input, &pos);

        // Ensure that the entire string was a valid integer
        if (pos != input.length()) {
            throw std::invalid_argument("Input contains non-integer characters.");
        }

        return number;
    } catch (const std::invalid_argument& e) {
        throw std::runtime_error("Invalid input: Not a valid integer.");
    } catch (const std::out_of_range& e) {
        throw std::runtime_error("Invalid input: Integer out of range.");
    }
}

int main(int argc, char* argv[]) {
    // Define an array of integers
    const int arr[] = {10, 20, 30, 40, 50};
    const int arrSize = sizeof(arr) / sizeof(arr[0]);

    // Check if a command-line argument is provided
    if (argc != 2) {
        std::cerr << "Error: Please provide a single integer as a command-line argument." << std::endl;
        return 1;
    }

    try {
        // Convert the argument to an integer
        int index = convertToInt(argv[1]);

        // Check if the index is within the array bounds
        if (index >= 0 && index < arrSize) {
            std::cout << "Element at index " << index << ": " << arr[index] << std::endl;
        } else {
            std::cerr << "Invalid input: Index out of bounds." << std::endl;
        }
    } catch (const std::runtime_error& e) {
        // Handle any conversion or validation errors
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
