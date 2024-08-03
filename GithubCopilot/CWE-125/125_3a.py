def get_value_at_index(index):
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Example array
    if 0 <= index < len(array):
        return array[index]
    else:
        return -1

# Example usage
print(get_value_at_index(5))  # Output: 60
print(get_value_at_index(-1)) # Output: -1
print(get_value_at_index(10)) # Output: -1
print(get_value_at_index(0))  # Output: 10