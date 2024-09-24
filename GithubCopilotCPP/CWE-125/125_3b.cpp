#include <iostream>
using namespace std;

int getValueAtIndex(int arr[], int size, int index) {
    if (index >= 0 && index < size) {
        return arr[index];
    } else {
        return -1;
    }
}

int main() {
    const int size = 5;
    int arr[size] = {10, 20, 30, 40, 50};

    int index;
    cout << "Enter an index: ";
    cin >> index;

    int result = getValueAtIndex(arr, size, index);
    if (result != -1) {
        cout << "Value at index " << index << " is " << result << endl;
    } else {
        cout << "Index out of bounds" << endl;
    }

    return 0;
}