def get_value_at_index(arr):
    # Input validation and sanitizing
    try:
        index = input("Please enter an index: ")
        # Sanitize input to ensure it's an integer
        index = int(index.strip())  # Strip removes leading/trailing spaces
    except ValueError:
        print("Error: Please enter a valid integer.")
        return -1

    # Array index bounds checking
    if index < 0 or index >= len(arr):
        print("Error: Index out of bounds.")
        return -1

    # Return value at index if no errors
    return arr[index]

# Example usage
arr = [10, 20, 30, 40, 50]
result = get_value_at_index(arr)
print("Value at index:", result)