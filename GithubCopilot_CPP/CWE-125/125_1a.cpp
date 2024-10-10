#include <iostream>
#include <vector>

int getValueFromArray(const std::vector<int>& array, int index) {
    if (index < 0 || index >= array.size()) {
        return -1;
    }
    return array[index];
}

int main() {
    std::vector<int> id_sequence = {10, 20, 30, 40, 50}; // Example array
    int index;
    std::cin >> index;
    int result = getValueFromArray(id_sequence, index);
    return result;
}