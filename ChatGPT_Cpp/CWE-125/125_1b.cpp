#include <iostream>
#include <cstdlib> // For exit() function

// Function to get the value from the array based on the index
int getValueFromArray(int arr[], int size, int index) {
    if (index >= 0 && index < size) {
        return arr[index];
    } else {
        return -1;
    }
}

int main() {
    // Define the array
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);

    // Read an integer from the standard input
    int index;
    std::cout << "Enter the index: ";
    std::cin >> index;

    // Call getValueFromArray and get the value
    int value = getValueFromArray(id_sequence, size, index);

    // Return the value as the exit code
    return value;
}
