# Define an array of vehicles
vehicles = ["Car", "Truck", "Motorcycle", "Bicycle", "Boat"]

# Prompt the user for the index of a vehicle
try:
    index = int(input("Enter the index of the vehicle you want to select (0-4): "))

    # Ensure the index is within the valid range
    if 0 <= index < len(vehicles):
        # Return the vehicle at the specified index
        selected_vehicle = vehicles[index]
        print(f"The vehicle at index {index} is: {selected_vehicle}")
    else:
        print("Index out of range. Please enter a valid index.")

except ValueError:
    print("Invalid input. Please enter an integer.")

# Loop through the array and print out each vehicle
print("\nList of all vehicles:")
for vehicle in vehicles:
    print(vehicle)
