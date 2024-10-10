import json

import os

import sys



# Secure data storage

def save_secure_data(data, filename="vehicles.json"):

    try:

        with open(filename, 'w') as file:

            json.dump(data, file)

    except IOError as e:

        print(f"An error occurred while writing to file: {e}")



def load_secure_data(filename="vehicles.json"):

    try:

        if os.path.exists(filename):

            with open(filename, 'r') as file:

                data = json.load(file)

                return data

        else:

            return []

    except IOError as e:

        print(f"An error occurred while reading from file: {e}")

        return []

    except json.JSONDecodeError as e:

        print(f"Error decoding JSON from file: {e}")

        return []



# Secure output

def secure_print(output):

    print(output.replace("<", "").replace(">", ""))



# Input validation

def validate_index(index, length):

    try:

        index = int(index)

        if 0 <= index < length:

            return True

    except ValueError:

        pass

    return False



# Safe exit

def safe_exit():

    print("Exiting the program. Goodbye!")

    sys.exit(0)



def main():

    vehicles = load_secure_data()

    if not vehicles:

        vehicles = ["Car", "Bike", "Truck", "Bus", "Motorcycle"]

        save_secure_data(vehicles)



    while True:

        try:

            index = input("Enter the index of the vehicle you want to retrieve (or 'q' to quit): ")

            if index.lower() == 'q':

                safe_exit()



            if not validate_index(index, len(vehicles)):

                raise ValueError("Index must be a valid integer within the range of available vehicles.")



            index = int(index)

            selected_vehicle = vehicles[index]

            secure_print(f"The vehicle at index {index} is: {selected_vehicle}")



            secure_print("List of all vehicles:")

            for i, vehicle in enumerate(vehicles):

                secure_print(f"Index {i}: {vehicle}")



        except ValueError as ve:

            secure_print(f"Value Error: {ve}")

        except IndexError:

            secure_print("Index Error: Index out of range.")

        except Exception as e:

            secure_print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":

    main()