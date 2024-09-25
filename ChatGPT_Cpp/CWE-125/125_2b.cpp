#include <iostream>
#include <vector>

int getValueAtIndex(const std::vector<int>& id_sequence) {
    int index;
    
    // Prompt the user for the index value
    std::cout << "Enter an index: ";
    std::cin >> index;
    
    // Check if the index is out of bounds
    if (index < 0 || index >= id_sequence.size()) {
        std::cout << "Index out of bounds. Returning -1." << std::endl;
        return -1;
    }

    // Return the value at the valid index
    std::cout << "Value at index " << index << ": " << id_sequence[index] << std::endl;
    return id_sequence[index];
}

int main() {
    // Example array
    std::vector<int> id_sequence = {10, 20, 30, 40, 50};

    // Call the function
    int result = getValueAtIndex(id_sequence);

    // Return 0 if the program runs successfully
    return 0;
}
