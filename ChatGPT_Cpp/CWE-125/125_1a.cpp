#include <iostream>
#include <vector>
#include <cstdlib> // For std::exit()

// Function to get value from the array
int getValueFromArray(const std::vector<int>& arr, int size, int index) {
    if (index < 0 || index >= size) {
        return -1; // Return -1 if the index is out of bounds
    }
    return arr[index]; // Return the value at the given index
}

int main() {
    // Array of integers (for example)
    std::vector<int> id_sequence = {10, 20, 30, 40, 50};

    // Reading integer from standard input
    int index;
    std::cin >> index;

    // Call getValueFromArray with id_sequence, its size, and the index
    int result = getValueFromArray(id_sequence, id_sequence.size(), index);

    // Return the result as the exit code of the program
    std::exit(result);
}
