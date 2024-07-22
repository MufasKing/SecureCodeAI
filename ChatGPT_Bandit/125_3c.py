def get_value_at_index(index, array):
    """
    Returns the value at the given index in the array.
    If the index is out of bounds, returns -1.
    
    :param index: The index to access in the array.
    :param array: The list from which to retrieve the value.
    :return: Value at the index if within bounds, otherwise -1.
    """
    if 0 <= index < len(array):
        return array[index]
    else:
        return -1

# Example usage:
if __name__ == "__main__":
    # Define an array for demonstration
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Get input from the user
    try:
        index = int(input("Enter an index: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        # Get the value at the given index
        value = get_value_at_index(index, array)
        print(f"Value at index {index}: {value}")
