#include <iostream>
#include <vector>

int getValueFromArray(const std::vector<int>& array, int index) {
    if (index >= 0 && index < array.size()) {
        return array[index];
    } else {
        return -1;
    }
}

int main() {
    std::vector<int> id_sequence = {10, 20, 30, 40, 50}; // Example array
    int index;
    std::cin >> index;

    int value = getValueFromArray(id_sequence, index);
    return value;
}