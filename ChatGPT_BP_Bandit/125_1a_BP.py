import sys

def getValueFromArray(array, size, index):
    # Check if index is within bounds
    if index < 0 or index >= size:
        return -1
    else:
        return array[index]

def main():
    # Initialize your array
    id_sequence = [1, 4, 6, 8, 10]
    size = len(id_sequence)

    try:
        # Read an integer from standard input
        input_index = int(input("Enter an index: ").strip())

        # Call the function getValueFromArray
        result = getValueFromArray(id_sequence, size, input_index)

        # Print the result (which will be the exit code)
        print(f"Result: {result}")
        sys.exit(result)

    except ValueError:
        print("Error: Input should be an integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()