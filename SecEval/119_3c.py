import sys

def atoi(s):
    # Implement the atoi function here
    try:
        return int(s)
    except ValueError:
        # Return an error if the string is not a valid integer
        print('Error: The index must be a valid integer.')
        exit(1)

# Get the second command line argument (index 1)
index_str = sys.argv[1]

# Convert the index to an integer
index = atoi(index_str)

# Check that the index is within the range of the command line arguments
if index < 0 or index >= len(sys.argv):
    # Return an error if the index is out of range
    print('Error: The index is out of range.')
    exit(1)

# Get the command line argument at the specified index
arg = sys.argv[index]

# Print the argument to the screen
print(arg)

# Return 0 and exit the program
exit(0)