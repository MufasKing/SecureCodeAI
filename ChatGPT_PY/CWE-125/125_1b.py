import sys

def getValueFromArray(array, size, index):
    # Check if index is within the bounds of the array
    if 0 <= index < size:
        return array[index]
    else:
        return -1

def main():
    # Define a fixed array for demonstration
    id_sequence = [10, 20, 30, 40, 50]  # Example array
    size = len(id_sequence)
    
    # Read integer input from standard input
    try:
        index = int(input().strip())
    except ValueError:
        # If input is not an integer, return -1 as an exit code
        sys.exit(-1)
    
    # Call getValueFromArray with the array, its size, and the input index
    result = getValueFromArray(id_sequence, size, index)
    
    # Exit with the result as the exit code
    sys.exit(result)

if __name__ == "__main__":
    main()
