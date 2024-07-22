def get_value_at_index(input_index):
    # Define the array
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    try:
        # Convert input to integer
        index = int(input_index)
        
        # Input validation
        if index < 0 or index >= len(array):
            return -1
        
        # Return the value at the specified index
        return array[index]
    except ValueError:
        # Handle case where input is not an integer
        return -1
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return -1

# Securely getting input as a string and stripping unwanted whitespace
user_input = input("Enter an index: ").strip()

# Call the function and print the result
result = get_value_at_index(user_input)
print(f"The value at the index is: {result}")