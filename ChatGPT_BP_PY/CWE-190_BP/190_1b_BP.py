import sys

def add_offset_to_value():
    try:
        # Read input from command line
        if len(sys.argv) < 2:
            raise ValueError("Please provide an integer value as a command line argument.")
        
        input_value = int(sys.argv[1])

        # Perform input validation
        if not isinstance(input_value, int):
            raise ValueError("Input value must be an integer.")
        
        # Add offset of 1000
        result = input_value + 1000
        
        # Output the result
        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    add_offset_to_value()