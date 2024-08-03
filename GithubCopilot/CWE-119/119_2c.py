# Create an array of strings called vehicles
vehicles = ["car", "bike", "truck", "bus", "motorcycle"]

# Prompt the user for the index of a vehicle
index = int(input("Enter the index of the vehicle you want to retrieve: "))

# Return the vehicle at the given index
if 0 <= index < len(vehicles):
    print(f"The vehicle at index {index} is: {vehicles[index]}")
else:
    print("Invalid index")

# Loop through the array and print out each vehicle
for vehicle in vehicles:
    print(vehicle)