def get_id_value(id_sequence):
    try:
        # Prompt the user for an index value
        index = int(input("Enter the index value: "))
        
        # Perform bounds checking
        if index < 0 or index >= len(id_sequence):
            print("Index out of bounds.")
            return 0
        
        # Return the value at the index if in bounds
        return id_sequence[index]
    except ValueError:
        # Handle non-integer inputs gracefully
        print("Invalid input. Please enter an integer.")
        return 0
    except Exception as e:
        # General exception handling to adhere to the principle of least privilege
        print(f"An unexpected error occurred: {e}")
        return 0