#include <iostream>
#include <cstdlib>  // For atoi()

int main(int argc, char* argv[]) {
    // Array of sample elements
    int arr[] = {10, 20, 30, 40, 50};
    int arraySize = sizeof(arr) / sizeof(arr[0]);

    // Check if a command-line argument was provided
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <index>\n";
        return 1;
    }

    // Convert the command-line argument to an integer
    int index = std::atoi(argv[1]);

    // Check if the index is within the valid range
    if (index >= 0 && index < arraySize) {
        std::cout << "Element at index " << index << " is: " << arr[index] << "\n";
    } else {
        std::cout << "Invalid input\n";
    }

    return 0;
}
