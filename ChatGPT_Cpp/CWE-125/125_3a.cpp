#include <iostream>

int getValueAtIndex(int arr[], int size, int index) {
    // Return -1 for invalid indices
    if (index < 0 || index >= size) {
        return -1;
    }
    return arr[index];
}

int main() {
    // Example array
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Input index
    int index;
    std::cout << "Enter the index: ";
    std::cin >> index;

    // Get the value at the index
    int result = getValueAtIndex(arr, size, index);

    // Output the result
    std::cout << "Value at index " << index << " is: " << result << std::endl;

    return 0;
}
