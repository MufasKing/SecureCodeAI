import sys

def getValueFromArray(arr, size, index):
    """
    Returns the value at the specified index if the index is within the bounds of the array.
    Otherwise, returns -1.
    """
    if 0 <= index < size:
        return arr[index]
    else:
        return -1

def main():
    try:
        # Reading an integer from standard input
        index = int(input("Enter an index: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return -1  # Exiting with -1 to indicate error

    # Example array, replace with actual array as needed
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)

    # Input validation
    if index < 0:
        print("Error: Index cannot be negative.")
        return -1

    # Calling the function with the user-provided index
    value = getValueFromArray(id_sequence, size, index)

    if value == -1:
        print("Index out of bounds.")
    else:
        print(f"Value at index {index}: {value}")

    # Returning the value as exit code, note: exit codes are typically used to indicate status, not data
    sys.exit(value)

if __name__ == "__main__":
    main()