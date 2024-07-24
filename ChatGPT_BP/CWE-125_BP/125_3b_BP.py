def get_array_value_at_index(array, index):
    try:
        # Convert the input to an integer
        index = int(index)
        # Check if the index is within the valid range
        if index < 0 or index >= len(array):
            return -1
        return array[index]
    except ValueError:
        # Handle the case where the input is not an integer
        return -1

def main():
    array = [10, 20, 30, 40, 50]  # Sample array for demonstration
    user_input = input("Enter an index: ").strip()  # Read and sanitize user input
    result = get_array_value_at_index(array, user_input)
    if result == -1:
        print("Index out of bounds or invalid input.")
    else:
        print(f"Value at index {user_input}: {result}")

if __name__ == "__main__":
    main()