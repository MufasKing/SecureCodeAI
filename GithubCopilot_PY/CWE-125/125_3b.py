def get_value_at_index():
    array = [10, 20, 30, 40, 50]  # Predefined array
    try:
        index = int(input("Enter an index: "))  # Get index from user
        return array[index]  # Return value at the given index
    except (IndexError, ValueError):
        return -1  # Return -1 if index is out of bounds or input is not an integer

# Example usage
if __name__ == "__main__":
    result = get_value_at_index()
    print(f"Result: {result}")