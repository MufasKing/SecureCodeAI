#include <iostream>
#include <string>

int main() {
    // Step 1: Define an array of strings called vehicles
    std::string vehicles[] = {"Car", "Bike", "Truck", "Bus", "Scooter"};
    int arraySize = sizeof(vehicles) / sizeof(vehicles[0]);

    // Step 2: Prompt the user to enter an index
    int index;
    std::cout << "Enter the index of the vehicle (0 to " << arraySize - 1 << "): ";
    std::cin >> index;

    // Step 3: Retrieve and print the vehicle at the specified index
    if (index >= 0 && index < arraySize) {
        std::cout << "Vehicle at index " << index << ": " << vehicles[index] << std::endl;
    } else {
        std::cout << "Invalid index!" << std::endl;
    }

    // Step 4: Loop through the array and print each vehicle
    std::cout << "List of all vehicles:" << std::endl;
    for (int i = 0; i < arraySize; ++i) {
        std::cout << vehicles[i] << std::endl;
    }

    return 0;
}