def get_value_at_index(id_sequence):
    try:
        index = int(input("Enter an index value: "))
        
        if index < 0 or index >= len(id_sequence):
            print("Index is out of bounds.")
            return -1
        
        value = id_sequence[index]
        print(f"Value at index {index} is: {value}")
        return 0
    
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")
        return -1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# Example usage:
id_sequence = [10, 20, 30, 40, 50]

# Test cases
get_value_at_index(id_sequence)