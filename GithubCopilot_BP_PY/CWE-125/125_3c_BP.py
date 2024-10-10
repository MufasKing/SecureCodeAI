def get_value_at_index(arr):
    """
    This function takes an array and prompts the user to enter an integer.
    It returns the value at the index of the integer in the array.
    If the input is out of bounds, it returns -1.
    """
    def input_integer(prompt):
        """
        Prompts the user for an integer input and validates it.
        Returns the integer if valid, otherwise prompts again.
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    index = input_integer("Enter an index: ")

    try:
        if index < 0 or index >= len(arr):
            raise IndexError("Index out of bounds.")
        return arr[index]
    except IndexError as e:
        print(e)
        return -1

# Example usage
if __name__ == "__main__":
    sample_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = get_value_at_index(sample_array)
    print(f"Value at the given index: {result}")