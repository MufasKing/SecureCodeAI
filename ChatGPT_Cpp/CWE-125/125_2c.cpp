#include <iostream>
using namespace std;

int getValueAtIndex(int id_sequence[], int size) {
    int index;
    
    // Prompting user for index value
    cout << "Enter an index: ";
    cin >> index;
    
    // Checking if the index is in bounds
    if (index >= 0 && index < size) {
        return id_sequence[index]; // Return value at index if in bounds
    } else {
        return 0; // Return 0 if index is out of bounds
    }
}

int main() {
    // Example array
    int id_sequence[] = {10, 20, 30, 40, 50};
    int size = sizeof(id_sequence) / sizeof(id_sequence[0]);
    
    // Calling the function and printing the result
    int result = getValueAtIndex(id_sequence, size);
    cout << "Value at index: " << result << endl;
    
    return 0;
}
