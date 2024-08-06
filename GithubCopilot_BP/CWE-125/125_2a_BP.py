def get_id_at_index(index, id_sequence):
    """
    This function takes an index and an array id_sequence.
    It returns the value at the given index in id_sequence.
    If the index is out of bounds, it returns -1.
    """
    try:
        # Ensure the index is an integer and within the bounds of id_sequence
        index = int(index)
        if index < 0 or index >= len(id_sequence):
            return -1
        return id_sequence[index]
    except ValueError:
        # Handle the case where the index is not an integer
        return -1
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return -1

def main():
    """
    Main function that prompts the user for an index value,
    calls get_id_at_index to get the value at that index in the array id_sequence,
    and prints the result.
    """
    id_sequence = [10, 20, 30, 40, 50]  # Example array, replace with actual id_sequence
    try:
        index = input("Enter an index value: ")
        result = get_id_at_index(index, id_sequence)
        if result == -1:
            print("Index out of bounds or invalid input.")
        else:
            print(f"The value at index {index} is {result}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()