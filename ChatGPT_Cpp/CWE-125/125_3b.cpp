#include <iostream>
using namespace std;

int getValueAtIndex(int arr[], int size, int index) {
    // Check if the index is out of bounds
    if (index < 0 || index >= size) {
        return -1; // Return -1 if out of bounds
    }
    return arr[index]; // Return the value at the specified index
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};  // Example array
    int size = sizeof(arr) / sizeof(arr[0]);  // Size of the array

    int index;
    cout << "Enter an index: ";
    cin >> index;

    int result = getValueAtIndex(arr, size, index);
    if (result == -1) {
        cout << "Index out of bounds!" << endl;
    } else {
        cout << "Value at index " << index << ": " << result << endl;
    }

    return 0;
}
