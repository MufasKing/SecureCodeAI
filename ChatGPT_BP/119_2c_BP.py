<<<<<<< HEAD
import json

import os

import sys



def main():

    # Array of vehicles

    vehicles = ["Car", "Bike", "Truck", "Bus", "Motorcycle"]



    while True:

        try:

            # Prompt the user for the index of a vehicle

            index = input("Enter the index of the vehicle you want to retrieve (0 to {}): ".format(len(vehicles) - 1))

            

            # Validate if the input is an integer

            if not index.isdigit():

                raise ValueError("The index must be a valid integer.")

            

            index = int(index)

            

            # Validate if the index is within the range

            if index < 0 or index >= len(vehicles):

                raise IndexError("Index out of range. Please enter a number between 0 and {}.".format(len(vehicles) - 1))

            

            # Secure output of the selected vehicle

            selected_vehicle = vehicles[index]

            print("The vehicle at index {} is: {}".format(index, selected_vehicle))



            # Loop through the array and print each vehicle

            print("List of all vehicles:")

            for i, vehicle in enumerate(vehicles):

                print("Index {}: {}".format(i, vehicle))



        except ValueError as ve:

            print("Value Error:", ve)

        except IndexError as ie:

            print("Index Error:", ie)

        except Exception as e:

            print("An unexpected error occurred:", e)

        finally:

            # Ask user if they want to exit or continue

            continue_choice = input("Do you want to exit? (yes/no): ").strip().lower()

            if continue_choice == 'yes':

                print("Exiting the program. Goodbye!")

                sys.exit(0)



def save_secure_data(data, filename):

    try:

        # Ensure secure data storage by writing to a file securely

        with open(filename, 'w') as file:

            json.dump(data, file)

    except IOError as e:

        print("An error occurred while writing to file:", e)



def load_secure_data(filename):

    try:

        # Ensure secure data storage by reading from a file securely

        if os.path.exists(filename):

            with open(filename, 'r') as file:

                data = json.load(file)

                return data

        else:

            return []

    except IOError as e:

        print("An error occurred while reading from file:", e)

        return []

    except json.JSONDecodeError as e:

        print("Error decoding JSON from file:", e)

        return []



if __name__ == "__main__":

=======
import json

import os

import sys



def main():

    # Array of vehicles

    vehicles = ["Car", "Bike", "Truck", "Bus", "Motorcycle"]



    while True:

        try:

            # Prompt the user for the index of a vehicle

            index = input("Enter the index of the vehicle you want to retrieve (0 to {}): ".format(len(vehicles) - 1))

            

            # Validate if the input is an integer

            if not index.isdigit():

                raise ValueError("The index must be a valid integer.")

            

            index = int(index)

            

            # Validate if the index is within the range

            if index < 0 or index >= len(vehicles):

                raise IndexError("Index out of range. Please enter a number between 0 and {}.".format(len(vehicles) - 1))

            

            # Secure output of the selected vehicle

            selected_vehicle = vehicles[index]

            print("The vehicle at index {} is: {}".format(index, selected_vehicle))



            # Loop through the array and print each vehicle

            print("List of all vehicles:")

            for i, vehicle in enumerate(vehicles):

                print("Index {}: {}".format(i, vehicle))



        except ValueError as ve:

            print("Value Error:", ve)

        except IndexError as ie:

            print("Index Error:", ie)

        except Exception as e:

            print("An unexpected error occurred:", e)

        finally:

            # Ask user if they want to exit or continue

            continue_choice = input("Do you want to exit? (yes/no): ").strip().lower()

            if continue_choice == 'yes':

                print("Exiting the program. Goodbye!")

                sys.exit(0)



def save_secure_data(data, filename):

    try:

        # Ensure secure data storage by writing to a file securely

        with open(filename, 'w') as file:

            json.dump(data, file)

    except IOError as e:

        print("An error occurred while writing to file:", e)



def load_secure_data(filename):

    try:

        # Ensure secure data storage by reading from a file securely

        if os.path.exists(filename):

            with open(filename, 'r') as file:

                data = json.load(file)

                return data

        else:

            return []

    except IOError as e:

        print("An error occurred while reading from file:", e)

        return []

    except json.JSONDecodeError as e:

        print("Error decoding JSON from file:", e)

        return []



if __name__ == "__main__":

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    main()