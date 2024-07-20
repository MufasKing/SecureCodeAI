def get_value_from_sequence():
    # Define the id_sequence array
    id_sequence = [10, 20, 30, 40, 50]  # Example values; you can customize this array
    
    # Prompt the user for an index value
    try:
        index = int(input("Enter the index value: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return 0
    
    # Check if the index is in bounds
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return 0

# Example usage:
result = get_value_from_sequence()
print(f"The value at the index is: {result}")
