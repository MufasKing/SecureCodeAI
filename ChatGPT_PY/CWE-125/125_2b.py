def get_value_at_index(id_sequence):
    """
    Prompts the user for an index value and returns the value at that index in the id_sequence array.
    
    Parameters:
    id_sequence (list): A list of values from which to retrieve a value based on user input.
    
    Returns:
    int: The value at the specified index, -1 if the index is out of bounds, and 0 if the function runs successfully.
    """
    try:
        # Prompt user for index value
        index = int(input("Enter the index value: "))
        
        # Check if index is within bounds
        if 0 <= index < len(id_sequence):
            return id_sequence[index]
        else:
            return -1
    
    except ValueError:
        # In case of invalid input that cannot be converted to an integer
        print("Invalid input. Please enter an integer.")
        return -1
    
    # Ensure the function returns 0 to signify successful completion
    return 0

# Example usage
id_sequence = [10, 20, 30, 40, 50]  # Example array
result = get_value_at_index(id_sequence)
print("Result:", result)
