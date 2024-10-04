import re

def get_vehicle(vehicles):
    """
    Prompts the user for the index of a vehicle and returns the vehicle at that index.
    Loops through the array and prints out each vehicle.
    """
    try:
        index = int(input("Enter the index of the vehicle you want: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

    if index < 0 or index >= len(vehicles):
        print("Index out of range. Please enter a number between 0 and", len(vehicles) - 1, ".")
        return None

    return vehicles[index]

vehicles = ['car', 'bike', 'truck', 'airplane', 'boat']

# Loop through the array and print each vehicle
for vehicle in vehicles:
    print(vehicle)

# Get the user input and return the vehicle
user_input = get_vehicle(vehicles)
if user_input:
    print("The selected vehicle is:", user_input)