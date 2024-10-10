def get_value_at_index():
    # Prompt the user for an index value
    index = int(input("Enter an index value: "))
    
    # Sample array
    id_sequence = [10, 20, 30, 40, 50]
    
    # Check if the index is within bounds
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return 0

# Example usage
print(get_value_at_index())