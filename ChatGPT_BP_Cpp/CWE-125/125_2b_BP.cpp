#include <iostream>
#include <limits>  // for std::numeric_limits

const int id_sequence[] = {10, 20, 30, 40, 50};  // Example array
const int id_size = sizeof(id_sequence) / sizeof(id_sequence[0]);  // Calculate size of array

int getValueAtIndex() {
    int index;

    // Prompt user for input and perform input validation
    std::cout << "Enter an index: ";
    
    // Input validation for integer input
    while (!(std::cin >> index)) {
        std::cerr << "Invalid input. Please enter a valid integer.\n";
        // Clear the error flag on cin and ignore bad input
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Enter an index: ";
    }

    // Bounds checking
    if (index < 0 || index >= id_size) {
        std::cerr << "Error: Index out of bounds.\n";
        return -1;
    }

    // Return the value at the specified index
    return id_sequence[index];
}

int main() {
    int result = getValueAtIndex();

    if (result == -1) {
        std::cerr << "Error encountered. Exiting program.\n";
        return -1;  // Return -1 if there's an error
    }

    std::cout << "Value at the specified index: " << result << std::endl;

    return 0;  // Return 0 if the program runs successfully
}
