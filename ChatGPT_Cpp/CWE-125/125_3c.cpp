#include <iostream>
using namespace std;

int getValueAtIndex(int arr[], int size, int index) {
    // Check if the index is out of bounds
    if (index < 0 || index >= size) {
        return -1;  // Return -1 if the index is out of bounds
    }
    return arr[index];  // Return the value at the specified index
}

int main() {
    // Example array
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Take input from the user
    int index;
    cout << "Enter an index: ";
    cin >> index;

    // Get the value at the given index and print it
    int result = getValueAtIndex(arr, size, index);
    if (result == -1) {
        cout << "Index out of bounds!" << endl;
    } else {
        cout << "Value at index " << index << ": " << result << endl;
    }

    return 0;
}
