def get_value_at_index(index, id_sequence):
    """
    Returns the value at the specified index in the id_sequence array.
    If the index is out of bounds, returns -1.
    """
    if 0 <= index < len(id_sequence):
        return id_sequence[index]
    else:
        return -1

def main():
    # Sample id_sequence array
    id_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    try:
        # Prompt the user for an index value
        user_input = int(input("Enter an index value: "))
        
        # Get the value at the index
        result = get_value_at_index(user_input, id_sequence)
        
        # Print the result
        print(f"The value at index {user_input} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
