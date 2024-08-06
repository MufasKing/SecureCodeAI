import sys

def atoi(s):
    try:
        return int(s)
    except ValueError:
        print("Error: Provided argument is not an integer.")
        sys.exit(1)

def get_command_line_argument(index):
    # Ensure index is within the range of command line arguments
    if index < 0 or index >= len(sys.argv):
        print(f"Error: Index {index} is out of range.")
        sys.exit(1)
    return sys.argv[index]

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <index> <value>")
        sys.exit(1)
    
    # Convert the second command line argument to an integer index
    index = atoi(sys.argv[1])
    
    # Get the command line argument at the specified index
    argument = get_command_line_argument(index)
    
    # Print the argument
    print(argument)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())