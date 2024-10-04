import re

# Define the array
_array = [10, 20, 30, 40, 50]

# Define a regular expression pattern to validate input
INPUT_PATTERN = r'^[-+]?[0-9]+$'

def get_value_at_index(user_input):
    """
    Validates and sanitizes the user input, checks if the index is within the array's range,
    and returns the value at the specified index or -1 if the input is invalid.
    """
    # Validate the input using the regular expression pattern
    if not re.match(INPUT_PATTERN, user_input):
        return -1

    # Sanitize the input by converting it to an integer
    index = int(user_input)

    # Check if the index is within the array's range
    if 0 <= index < len(_array):
        return _array[index]
    else:
        return -1

# Example usage
user_input = input("Enter an index: ")
result = get_value_at_index(user_input)
print(f"Value at the given index: {result}")