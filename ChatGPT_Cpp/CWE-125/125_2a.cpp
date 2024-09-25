#include <iostream>
using namespace std;

// Function to get value at a given index from id_sequence array
int getValueAtIndex(int index, const int id_sequence[], int size) {
    if (index >= 0 && index < size) {
        return id_sequence[index];
    } else {
        return -1; // Return -1 if the index is out of bounds
    }
}

int main() {
    const int id_sequence[] = {10, 20, 30, 40, 50}; // Array id_sequence
    const int size = sizeof(id_sequence) / sizeof(id_sequence[0]); // Size of the array

    int index;
    cout << "Enter an index: ";
    cin >> index;

    // Call the function and display the result
    int result = getValueAtIndex(index, id_sequence, size);
    
    if (result != -1) {
        cout << "Value at index " << index << " is: " << result << endl;
    } else {
        cout << "Index out of bounds!" << endl;
    }

    return 0;
}
