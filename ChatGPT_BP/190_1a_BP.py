import sys

def add_1000_to_input(input_value):
    try:
        # Convert input to integer
        number = int(input_value)
        
        # Add 1000 to the input number
        result = number + 1000
        
        # Print the result securely
        print(f"Result: {result}")
        
    except ValueError:
        # Handle the case where input is not a valid integer
        print("Error: Please enter a valid integer.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
    else:
        input_value = sys.argv[1]
        add_1000_to_input(input_value)