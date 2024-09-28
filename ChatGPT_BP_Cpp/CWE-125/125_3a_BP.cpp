#include <iostream>
#include <vector>
#include <limits>

// Function to safely get an integer input from the user
int getInput() {
    int input;
    while (true) {
        std::cout << "Enter an index: ";
        std::cin >> input;

        // Check if the input is a valid integer
        if (std::cin.fail()) {
            std::cin.clear();  // Clear the error state
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // Discard invalid input
            std::cout << "Invalid input. Please enter a valid integer.\n";
        } else {
            break;
        }
    }
    return input;
}

// Function to return the value at the specified index, or -1 for invalid input
int getValueAtIndex(const std::vector<int>& arr, int index) {
    if (index < 0 || index >= arr.size()) {
        return -1;  // Return -1 if index is out of bounds
    }
    return arr[index];  // Return the value at the valid index
}

int main() {
    // Initialize a sample vector with some values
    std::vector<int> myArray = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    // Get input from the user
    int index = getInput();

    // Check bounds and print the value or error
    int result = getValueAtIndex(myArray, index);

    if (result == -1) {
        std::cout << "Invalid index! Returning: " << result << std::endl;
    } else {
        std::cout << "Value at index " << index << ": " << result << std::endl;
    }

    return 0;
}
