# List of vehicles
vehicles = ["Car", "Bike", "Truck", "Bus", "Scooter"]

# Prompt the user to enter an index
index = input("Enter the index of the vehicle: ")

try:
    # Convert the index to an integer
    index = int(index)
    
    # Access the vehicle at the given index and print it
    print(f"The vehicle at index {index} is {vehicles[index]}")
except (ValueError, IndexError):
    print("Invalid index. Please enter a valid integer within the range of the vehicle list.")