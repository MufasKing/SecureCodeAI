def get_vehicle_index():
    """
    Prompts the user to enter an index and returns the index as an integer.
    Includes input validation to ensure the entered value is a valid integer.
    """
    while True:
        try:
            index = int(input("Enter the index of the vehicle: "))
            return index
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_vehicle_at_index(vehicles, index):
    """
    Prints the vehicle at the given index if the index is valid.
    Includes error handling to ensure the index is within the bounds of the list.
    """
    try:
        vehicle = vehicles[index]
        print(f"Vehicle at index {index}: {vehicle}")
    except IndexError:
        print("Index out of range. Please enter a valid index.")

def main():
    """
    Main function that orchestrates the user input and printing of the vehicle.
    """
    vehicles = ['Car', 'Bike', 'Truck', 'Boat', 'Plane']  # Example vehicle list
    index = get_vehicle_index()
    print_vehicle_at_index(vehicles, index)

if __name__ == "__main__":
    main()