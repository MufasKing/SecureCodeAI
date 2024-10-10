#include <iostream>
#include <vector>

// Define the array id_sequence
std::vector<int> id_sequence = {10, 20, 30, 40, 50};

// Function to get value at a given index
int getValueAtIndex(int index) {
    if (index >= 0 && index < id_sequence.size()) {
        return id_sequence[index];
    } else {
        return -1;
    }
}

int main() {
    int index;
    std::cout << "Enter an index value: ";
    std::cin >> index;

    int value = getValueAtIndex(index);
    if (value != -1) {
        std::cout << "Value at index " << index << " is " << value << std::endl;
    } else {
        std::cout << "Index out of bounds" << std::endl;
    }

    return 0;
}