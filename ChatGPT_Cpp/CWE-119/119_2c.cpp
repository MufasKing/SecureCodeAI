#include <iostream>
#include <string>
using namespace std;

int main() {
    // Create an array of strings called vehicles
    string vehicles[] = {"Car", "Bike", "Truck", "Bus", "Train"};
    int arraySize = sizeof(vehicles) / sizeof(vehicles[0]);

    // Prompt the user for the index of a vehicle
    int index;
    cout << "Enter the index of the vehicle (0 to " << arraySize - 1 << "): ";
    cin >> index;

    // Check if the index is within bounds
    if (index >= 0 && index < arraySize) {
        cout << "You selected: " << vehicles[index] << endl;
    } else {
        cout << "Invalid index!" << endl;
    }

    // Loop through the array and print out each vehicle
    cout << "\nList of vehicles:" << endl;
    for (int i = 0; i < arraySize; ++i) {
        cout << vehicles[i] << endl;
    }

    return 0;
}
