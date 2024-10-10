import sys

def getValueFromArray(arr, size, index):
    # Input validation
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Array must be a list of integers")
    if not isinstance(size, int) or size < 0:
        raise ValueError("Size must be a non-negative integer")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    
    # Check if index is within the bounds of the array
    if 0 <= index < size:
        return arr[index]
    else:
        return -1

def main():
    try:
        # Read an integer from standard input
        input_index = int(input("Enter an index: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return -1  # Exit code for invalid input
    
    # Example array, replace with actual array if needed
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    # Call getValueFromArray and return its value as exit code
    result = getValueFromArray(id_sequence, size, input_index)
    return result

if __name__ == "__main__":
    sys.exit(main())