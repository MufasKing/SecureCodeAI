#include <iostream>
#include <vector>

int getValueAtIndex(const std::vector<int>& arr, int index) {
    if (index >= 0 && index < arr.size()) {
        return arr[index];
    } else {
        return -1;
    }
}

int main() {
    std::vector<int> arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int index;

    std::cout << "Enter an index: ";
    std::cin >> index;

    int result = getValueAtIndex(arr, index);
    if (result != -1) {
        std::cout << "Value at index " << index << " is " << result << std::endl;
    } else {
        std::cout << "Index out of bounds" << std::endl;
    }

    return 0;
}