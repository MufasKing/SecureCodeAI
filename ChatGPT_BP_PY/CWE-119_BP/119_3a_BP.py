import sys

def atoi(s):
    """
    Converts a string to an integer.
    Raises ValueError if the string is not a valid integer.
    """
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Invalid integer value: '{s}'")

def get_argument(index, arguments):
    """
    Returns the argument at the specified index from the command line arguments.
    Raises IndexError if the index is out of range.
    """
    try:
        return arguments[index]
    except IndexError:
        raise IndexError(f"Argument index {index} is out of range")

def main():
    # Ensure there are enough command line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <index>")
        return 1

    try:
        # Convert the second argument to an integer index
        index = atoi(sys.argv[1])

        # Get the argument at the specified index
        argument = get_argument(index, sys.argv)

        # Print the argument
        print(argument)
        return 0

    except ValueError as ve:
        print(ve)
        return 1
    except IndexError as ie:
        print(ie)
        return 1

if __name__ == "__main__":
    sys.exit(main())