import sys

def getValueFromArray(array, size, index):
    if 0 <= index < size:
        return array[index]
    else:
        return -1

def main():
    # Example array and size
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    # Read integer from standard input
    try:
        index = int(input("Enter an index: ").strip())
    except ValueError:
        # If the input is not an integer, return -1
        index = -1
    
    # Get value from array
    result = getValueFromArray(id_sequence, size, index)
    
    # Exit with the result code
    sys.exit(result)

if __name__ == "__main__":
    main()
