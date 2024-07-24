import sys

def print_argv_index(index):
    # Check if index is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: Index argument is missing.")
        return
    
    try:
        index = int(index)  # Convert index to integer
        if index < 1 or index >= len(sys.argv):
            print(f"Error: Index {index} is out of range.")
        else:
            print(f"Argument at index {index} is: {sys.argv[index]}")
    except ValueError:
        print("Error: Index argument must be an integer.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python argv_index.py <index>")
    else:
        print_argv_index(sys.argv[1])