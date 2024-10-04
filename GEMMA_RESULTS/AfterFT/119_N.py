import re

# Input validation function
def is_valid_index(index, length):
    try:
        index = int(index)
        if 0 <= index < length:
            return True
    except ValueError:
        pass
    return False

# Secure string input function
def get_input(prompt):
    while True:
        try:
            return input(prompt)
        except SyntaxError:
            print("Invalid input. Please try again.")

# Main program
if __name__ == "__main__":
    # Initialize the items array
    items = ['Hat', 'Shirt', 'Pants', 'Shoes']

    while True:
        try:
            # Ask the user for an index
            index_input = get_input("Please enter the index of an item (0-{}): ".format(len(items) - 1))

            # Validate the input
            if not is_valid_index(index_input, len(items)):
                print("Invalid index. Please try again.")
                continue

            # Retrieve the item from the array
            item = items[int(index_input)]

            # Display the item
            print("Item at index {}: {}".format(index_input, item))

            # Iterate through the array and print each item sequentially
            for i, element in enumerate(items):
                print("Item at index {}: {}".format(i, element))

        except Exception as e:
            print("An error occurred:", str(e))
        
        # Ask the user if they want to exit or continue
        continue_input = get_input("Do you want to exit? (y/n): ")
        if re.match("^[Yy]$", continue_input):
            print("Exiting the program.")
            break
        else:
            print("Continuing with the program.")