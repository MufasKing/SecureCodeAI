#include <iostream>
#include <string>

int main() {
    // Array of vehicles
    std::string vehicles[] = {"Car", "Truck", "Motorcycle", "Bicycle", "Bus"};
    int numVehicles = sizeof(vehicles) / sizeof(vehicles[0]);
    
    // Prompt the user for an index
    std::cout << "Enter an index of a vehicle (0 to " << numVehicles - 1 << "): ";
    
    // Input index
    std::string input;
    std::cin >> input;
    
    // Convert input to integer
    int index = std::stoi(input);
    
    // Validate index and access array
    if (index >= 0 && index < numVehicles) {
        std::cout << "Vehicle at index " << index << ": " << vehicles[index] << std::endl;
    } else {
        std::cout << "Invalid index. Please enter a number between 0 and " << numVehicles - 1 << "." << std::endl;
    }

    return 0;
}
