def get_value_at_index(index):
    # Define the array
    array = [10, 20, 30, 40, 50]

    # Check if the index is within the bounds of the array
    if 0 <= index < len(array):
        return array[index]
    else:
        return -1

# Get user input
try:
    user_input = int(input("Enter the index: "))
    result = get_value_at_index(user_input)
    print(f"The value at index {user_input} is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
