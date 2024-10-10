import sys

def atoi(s):
    """Convert a string to an integer."""
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Invalid input for integer conversion: '{s}'")

def main():
    argc = len(sys.argv)
    argv = sys.argv
    
    # Print number of arguments
    print(f"Number of arguments: {argc}")

    # Print the program name and arguments
    print(f"Program name: {argv[0]}")
    print("Arguments:")
    
    for i in range(1, argc):
        print(f"argv[{i}] = {argv[i]}")
        try:
            # Convert argument to integer
            num = atoi(argv[i])
            print(f"  Converted to integer: {num}")
        except ValueError as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    main()
