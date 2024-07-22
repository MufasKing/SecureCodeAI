def get_value_at_index(index):
    # Define the array with some sample values
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Check if the index is valid for the array or not
    if index < 0 or index >= len(array):
        return -1
    else:
        return array[index]

# Example usage
try:
    # Get input from the user
    user_input = int(input("Enter an integer: "))
    # Call the function and print the result
    result = get_value_at_index(user_input)
    print(result)
except ValueError:
    print("Invalid input. Please enter an integer.")
