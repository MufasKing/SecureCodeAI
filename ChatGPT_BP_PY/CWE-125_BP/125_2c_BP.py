def get_value_at_index(id_sequence):
    try:
        # Prompt the user for an index value
        index = input("Please enter an index value: ")
        
        # Validate if the input is an integer
        index = int(index)
        
        # Check if the index is within bounds
        if 0 <= index < len(id_sequence):
            return id_sequence[index]
        else:
            # Return 0 if the index is out of bounds
            return 0
    except ValueError:
        # Handle the exception if input is not an integer
        print("Invalid input. Please enter a valid integer.")
        return 0

# Example usage:
id_sequence = [10, 20, 30, 40, 50]
value = get_value_at_index(id_sequence)
print("Value at index:", value)