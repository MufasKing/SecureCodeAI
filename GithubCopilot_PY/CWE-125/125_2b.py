def get_value_at_index():
    id_sequence = [10, 20, 30, 40, 50]  # Example array
    try:
        index = int(input("Enter an index value: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return -1

    if index < 0 or index >= len(id_sequence):
        return -1
    else:
        return id_sequence[index]

    return 0  # This line will never be reached

# Example usage
result = get_value_at_index()
print(f"Result: {result}")