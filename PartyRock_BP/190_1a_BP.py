import sys
import re
 
def validate_input(value):
    # Define a regular expression pattern to match valid numeric input
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    # Check if the input matches the pattern
    if re.match(pattern, value):
        return True
    else:
        return False
 
def secure_output(result):
    # Sanitize the output to prevent Code Injection and Cross-Site Scripting (XSS) attacks
    sanitized_result = str(result).replace("<", "&lt;").replace(">", "&gt;")
    print(sanitized_result)
 
def main():
    try:
        # Get the input value from the command line arguments
        if len(sys.argv) < 2:
            print("Error: Please provide a value as a command line argument.")
            sys.exit(1)
        input_value = sys.argv[1]
        # Validate the input
        if not validate_input(input_value):
            print("Error: Invalid input. Please provide a valid numeric value.")
            sys.exit(1)
        # Convert the input to a float
        value = float(input_value)
        # Add 1000 to the value
        result = value + 1000
        # Output the result securely
        secure_output(result)
    except ValueError:
        print("Error: Invalid input. Please provide a valid numeric value.")
    except Exception as e:
        print(f"Error: {str(e)}")
 
if __name__ == "__main__":
    main()