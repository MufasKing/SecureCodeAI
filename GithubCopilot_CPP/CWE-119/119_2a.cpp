#include <iostream>
#include <string>
#include <vector>

int main() {
    // Define an array of vehicles
    std::vector<std::string> vehicles = {"Car", "Bike", "Truck", "Bus", "Scooter"};

    // Prompt the user to enter an index
    std::cout << "Enter the index of the vehicle: ";
    std::string input;
    std::getline(std::cin, input);

    // Convert the input to an integer
    int index = std::stoi(input);

    // Check if the index is within the valid range
    if (index >= 0 && index < vehicles.size()) {
        // Print the vehicle at the given index
        std::cout << "Vehicle at index " << index << " is: " << vehicles[index] << std::endl;
    } else {
        std::cout << "Invalid index!" << std::endl;
    }

    return 0;
}