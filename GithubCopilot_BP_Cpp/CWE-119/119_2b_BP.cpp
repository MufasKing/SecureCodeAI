#include <iostream>
#include <string>
#include <stdexcept>

int main(int argc, char* argv[]) {
    // Define an array of integers
    int arr[] = {10, 20, 30, 40, 50};
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    // Check if the correct number of arguments is provided
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <index>" << std::endl;
        return 1;
    }

    try {
        // Convert the command-line argument to an integer
        int index = std::stoi(argv[1]);

        // Validate the index
        if (index >= 0 && index < arrSize) {
            std::cout << "Element at index " << index << " is " << arr[index] << std::endl;
        } else {
            std::cerr << "invalid input" << std::endl;
        }
    } catch (const std::invalid_argument& e) {
        std::cerr << "invalid input" << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "invalid input" << std::endl;
    }

    return 0;
}