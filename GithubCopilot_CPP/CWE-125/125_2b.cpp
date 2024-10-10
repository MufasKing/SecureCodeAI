#include <iostream>
#include <vector>

int getValueAtIndex(const std::vector<int>& id_sequence) {
    int index;
    std::cout << "Enter an index value: ";
    std::cin >> index;

    if (index < 0 || index >= id_sequence.size()) {
        return -1;
    }

    return id_sequence[index];
}

int main() {
    std::vector<int> id_sequence = {10, 20, 30, 40, 50}; // Example array
    int result = getValueAtIndex(id_sequence);

    if (result == -1) {
        std::cout << "Index out of bounds." << std::endl;
    } else {
        std::cout << "Value at index: " << result << std::endl;
    }

    return 0;
}