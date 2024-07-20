import sys

def atoi(s):
    """Convert a string to an integer."""
    try:
        return int(s)
    except ValueError:
        print(f"Error: '{s}' is not a valid integer.")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <index> <arg1> <arg2> ...")
        sys.exit(1)
    
    # The second argument is at index 1
    index_arg = sys.argv[1]

    # Convert the second argument (index) to an integer
    try:
        index = atoi(index_arg)
    except ValueError:
        print(f"Error: Invalid index '{index_arg}'")
        sys.exit(1)

    # Ensure the index is within the range of command line arguments
    if index < 2 or index >= len(sys.argv):
        print(f"Error: Index {index} is out of range.")
        sys.exit(1)

    # Retrieve the argument at the specified index
    argument = sys.argv[index]
    
    # Print the argument
    print(argument)
    
    # Exit the program with return code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
