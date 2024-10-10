# Define a function to prompt the user for an index and return the selected vehicle
def get_vehicle_by_index(vehicles):
    while True:
        try:
            # Prompt the user for an index
            index_input = input("Please enter the index of the vehicle you want to access: ")
            # Convert the input to an integer
            index = int(index_input)
            # Access the vehicle at the given index
            vehicle = vehicles[index]
            return vehicle
        except ValueError:
            # Handle non-integer inputs
            print("Error: Please enter a valid integer.")
        except IndexError:
            # Handle out-of-range inputs
            print(f"Error: Please enter an index between 0 and {len(vehicles) - 1}.")

# Main function to drive the program
def main():
    # Example array of vehicles
    vehicles = ["Car", "Truck", "Bicycle", "Motorcycle", "Bus"]
    
    # Get the selected vehicle
    selected_vehicle = get_vehicle_by_index(vehicles)
    
    # Print the selected vehicle
    print(f"The selected vehicle is: {selected_vehicle}")

if __name__ == "__main__":
    main()