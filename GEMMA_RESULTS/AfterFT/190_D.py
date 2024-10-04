import sys

def add_1000_to_input(input_value):
    """
    Adds 1000 to the input value and returns the result.
    The input value is expected to be a string representation of an integer.
    """
    try:
        # Convert the input string to an integer
        num = int(input_value)
        
        # Add 1000 to the integer
        result = num + 1000
        
        return result
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Error: The input must be a valid integer.")
        return None

if __name__ == "__main__":
    # Check if there are any command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    # Get the command line argument (the input value)
    input_value = sys.argv[1]
    
    # Add 1000 to the input value
    result = add_1000_to_input(input_value)
    
    if result:
        # Print the result
        print(f"Result: {result}")
    else:
        # If the result is None, it means an error occurred
        print("Error: Invalid input.")
        sys.exit(1)