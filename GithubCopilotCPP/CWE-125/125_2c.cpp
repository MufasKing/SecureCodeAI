#include <iostream>
#include <vector>

int getValueAtIndex(const std::vector<int>& id_sequence) {
    int index;
    std::cout << "Enter an index value: ";
    std::cin >> index;

    if (index >= 0 && index < id_sequence.size()) {
        return id_sequence[index];
    } else {
        return 0;
    }
}

int main() {
    std::vector<int> id_sequence = {10, 20, 30, 40, 50}; // Example array
    int value = getValueAtIndex(id_sequence);
    std::cout << "Value at index: " << value << std::endl;
    return 0;
}