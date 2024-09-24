#include <iostream>
#include <cstdlib> // For atoi

int main(int argc, char* argv[]) {
    // Check if there is exactly one command line argument
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <index>" << std::endl;
        return 1;
    }

    // Convert the command line argument to an integer
    int index = std::atoi(argv[1]);

    // Define an array with some elements
    int arr[] = {10, 20, 30, 40, 50};
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    // Check if the index is within the range of the array
    if (index >= 0 && index < arrSize) {
        std::cout << "Element at index " << index << " is " << arr[index] << std::endl;
    } else {
        std::cout << "invalid input" << std::endl;
    }

    return 0;
}