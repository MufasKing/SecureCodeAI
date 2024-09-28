#include <iostream>
#include <limits> // For input validation

// Function to safely get an integer from user
int getIntegerInput() {
    int input;
    while (true) {
        std::cout << "Enter an index: ";
        std::cin >> input;
        
        // Input validation
        if (std::cin.fail()) {
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << "Invalid input. Please enter an integer." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear extra input
            return input;
        }
    }
}

// Function to return the value at the index if valid, else return -1
int getValueAtIndex(const int arr[], size_t size, int index) {
    // Bounds checking
    if (index >= 0 && index < static_cast<int>(size)) {
        return arr[index];
    } else {
        std::cerr << "Error: Index out of bounds." << std::endl;
        return -1; // Return -1 if index is out of bounds
    }
}

int main() {
    // Example array
    const int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    const size_t arraySize = sizeof(arr) / sizeof(arr[0]); // Get array size

    // Get valid integer input
    int index = getIntegerInput();

    // Get the value at the input index or handle error
    int value = getValueAtIndex(arr, arraySize, index);

    // Display the result
    if (value != -1) {
        std::cout << "Value at index " << index << " is: " << value << std::endl;
    } else {
        std::cout << "Invalid index provided." << std::endl;
    }

    return 0;
}
