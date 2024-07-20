def getValueFromArray(arr, size, index):
    """
    Returns the value at the given index in the array if index is within bounds,
    otherwise returns -1.
    
    Parameters:
    arr (list): The array of integers.
    size (int): The size of the array.
    index (int): The index to retrieve value from.
    
    Returns:
    int: Value at the given index or -1 if index is out of bounds.
    """
    try:
        if 0 <= index < size:
            return arr[index]
        else:
            return -1
    except TypeError:
        return -1  # In case arr is not a list or index is not an integer


def main():
    try:
        id_sequence = [1, 2, 3, 4, 5]  # Example array, you can modify this
        size = len(id_sequence)
        
        # Read an integer input
        try:
            input_index = int(input("Enter an index: "))
        except ValueError:
            print("Error: Please enter a valid integer.")
            return
        
        # Call getValueFromArray and capture the return value
        result = getValueFromArray(id_sequence, size, input_index)
        
        # Return the result as the exit code
        exit(result)
    
    except Exception as e:
        print(f"Error: {e}")
        exit(-1)

if __name__ == "__main__":
    main()