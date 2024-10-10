import sys

# Define the offset constant
OFFSET = 1000

def main():
    if len(sys.argv) != 2:
        print("Usage: python 190_1b.py <number>")
        sys.exit(1)
    
    try:
        # Read the value from the command line
        value = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
    
    # Add the offset to the value
    result = value + OFFSET
    
    # Print the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()