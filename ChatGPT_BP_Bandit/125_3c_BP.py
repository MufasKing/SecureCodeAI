def get_value_at_index(array, index):
    """
    This function returns the value at the specified index in the array.
    If the index is out of bounds, it returns -1.

    :param array: List of values
    :param index: Index to retrieve the value from
    :return: Value at the index or -1 if out of bounds
    """
    try:
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(array):
            return -1
        return array[index]
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return -1

def main():
    # Example array
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    try:
        # User input
        user_input = input("Enter an index: ")
        
        # Validate and convert input to an integer
        index = int(user_input)
        
        # Get the value at the specified index
        result = get_value_at_index(array, index)
        
        # Display the result
        print(f"Value at index {index}: {result}")
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()