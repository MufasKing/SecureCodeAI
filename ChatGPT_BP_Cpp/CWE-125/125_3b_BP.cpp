#include <iostream>
#include <vector>
#include <limits> // for numeric_limits

// Class encapsulating the functionality
class ArrayHandler {
private:
    std::vector<int> data; // Encapsulated data member

public:
    // Constructor to initialize the vector with some values
    ArrayHandler() {
        data = {10, 20, 30, 40, 50}; // Example data
    }

    // Function to safely get the value at a specific index
    int getValueAtIndex(int index) {
        if (index < 0 || index >= data.size()) {
            std::cerr << "Error: Index out of bounds.\n";
            return -1;
        }
        return data[index];
    }

    // Function to take input from the user and validate it
    int getValidatedInput() {
        int index;
        while (true) {
            std::cout << "Enter an index (0 to " << data.size() - 1 << "): ";
            std::cin >> index;

            // Input validation: Check if input is an integer
            if (std::cin.fail()) {
                std::cin.clear(); // Clear the error state
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore invalid input
                std::cerr << "Invalid input. Please enter a valid integer.\n";
            } else {
                break; // Valid input, exit the loop
            }
        }
        return index;
    }

    // Function to handle the overall process
    void handleInputAndOutput() {
        int index = getValidatedInput();
        int result = getValueAtIndex(index);

        if (result != -1) {
            std::cout << "Value at index " << index << " is: " << result << "\n";
        }
    }
};

int main() {
    ArrayHandler handler;
    handler.handleInputAndOutput();

    return 0;
}
