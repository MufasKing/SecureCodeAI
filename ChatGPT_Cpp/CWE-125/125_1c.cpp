#include <iostream>
#include <cstdlib> // For exit()

// Function to get value from the array based on the index
int getValueFromArray(const int array[], int size, int index) {
    if (index >= 0 && index < size) {
        return array[index];
    } else {
        return -1; // Return -1 if index is out of bounds
    }
}

int main() {
    // Sample array
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);

    // Read index from standard input
    int index;
    std::cout << "Enter index: ";
    std::cin >> index;

    // Get the value from the array
    int result = getValueFromArray(id_sequence, size, index);

    // Return the result as exit code
    return result;
}
