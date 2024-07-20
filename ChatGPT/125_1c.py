import sys

def getValueFromArray(arr, size, index):
    """
    Retrieve the value from the array at the specified index if it is within bounds.
    Otherwise, return -1.
    """
    if 0 <= index < size:
        return arr[index]
    else:
        return -1

def main():
    # Sample array of integers and its size
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    # Read an integer from standard input
    try:
        index = int(input("Enter the index: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)  # Exit with code 1 to indicate error in input
    
    # Get the value from the array using the provided index
    value = getValueFromArray(id_sequence, size, index)
    
    # Return the value as the exit code
    sys.exit(value)

if __name__ == "__main__":
    main()
