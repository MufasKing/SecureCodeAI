import sys

def main():
    # Constant offset value
    OFFSET = 1000
    
    # Check if a command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        # Attempt to convert the command line argument to an integer
        input_value = int(sys.argv[1])
    except ValueError:
        # Handle the case where the conversion fails
        print("Error: The provided value must be an integer.")
        sys.exit(1)
    
    # Add the offset to the input value
    result = input_value + OFFSET
    
    # Print the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()