#include <iostream>
using namespace std;

int main() {
    // Define an array with some sample values
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Take an integer input from the user
    int index;
    cout << "Enter an index: ";
    cin >> index;

    // Check if the input is within the valid range of the array indices
    if (index >= 0 && index < size) {
        // Return the value at that index
        cout << "Value at index " << index << " is " << arr[index] << endl;
    } else {
        // Return -1 if the input is out of range
        cout << -1 << endl;
    }

    return 0;
}