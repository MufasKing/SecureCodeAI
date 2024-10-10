import sys

def main():
    # Check if there are enough arguments
    if len(sys.argv) < 2:
        print("Usage: python argv_index.py <index>")
        sys.exit(1)
    
    # Parse the index argument
    try:
        index = int(sys.argv[1])
    except ValueError:
        print("The index must be an integer.")
        sys.exit(1)
    
    # Check if the index is within the valid range
    if index < 1 or index >= len(sys.argv):
        print(f"Index {index} is out of range. Please provide a valid index.")
        sys.exit(1)
    
    # Print the corresponding command-line argument
    print(sys.argv[index])

if __name__ == "__main__":
    main()
