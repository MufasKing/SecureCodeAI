import sys

def getValueFromArray(arr, size, index):
    """
    This function takes an array of integers, its size, and an index as parameters.
    It checks if the index is within the bounds of the array. If not, it returns -1.
    Otherwise, it returns the value at the given index.
    """
    # Array bounds checking
    if index < 0 or index >= size:
        return -1
    else:
        return arr[index]

def main():
    """
    The main function reads an integer from the standard input and calls getValueFromArray
    with the id_sequence array, its size, and the read integer. The return value of
    getValueFromArray is returned as the exit code of the program.
    """
    # Sample array for demonstration. Replace with actual array as needed.
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    try:
        # Reading integer from standard input and performing input validation
        index = int(input("Enter an index: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        sys.exit(1)  # Exiting with error code 1 to indicate input error
    
    # Calling getValueFromArray and handling the return value
    value = getValueFromArray(id_sequence, size, index)
    
    if value == -1:
        print("Index out of bounds.")
        sys.exit(2)  # Exiting with error code 2 to indicate out of bounds error
    else:
        print(f"Value at index {index}: {value}")
        sys.exit(0)  # Exiting with code 0 to indicate successful execution

if __name__ == "__main__":
    main()