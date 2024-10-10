def get_value_at_index(arr):
    """
    This function takes an integer as input and returns the value at the index of the integer in the array.
    If the input is -1 or out of the array's bounds, it returns -1.
    It performs input validation, secure string operations, and exception handling.
    """
    try:
        # Input validation
        index = input("Please enter an integer index: ")
        if not index.isdigit() and not (index.startswith('-') and index[1:].isdigit()):
            raise ValueError("Input is not a valid integer.")

        index = int(index)

        # Check for valid index range
        if index == -1 or index >= len(arr):
            return -1

        # Secure string operation: Ensure index is within bounds
        if 0 <= index < len(arr):
            return arr[index]
        else:
            return -1
    except ValueError as e:
        print(f"Error: {e}")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1

# Example usage
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = get_value_at_index(arr)
print(f"Result: {result}")