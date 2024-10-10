# Define a list of vehicles
vehicles = ["Car", "Motorcycle", "Bicycle", "Bus", "Truck"]

# Prompt the user to enter an index
user_input = input("Enter the index of the vehicle you want to access (0 to {}): ".format(len(vehicles) - 1))

try:
    # Convert the user input to an integer
    index = int(user_input)

    # Check if the index is within the valid range
    if 0 <= index < len(vehicles):
        # Access and print the vehicle at the given index
        print("The vehicle at index {} is: {}".format(index, vehicles[index]))
    else:
        print("Error: Index is out of range. Please enter a number between 0 and {}.".format(len(vehicles) - 1))

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
