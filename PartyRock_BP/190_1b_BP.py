import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide one argument (a number) as a command line argument.")
        return

    input_value = sys.argv[1]

    # Input Validation
    if not input_value.isdigit():
        print("Error: Input must be a valid integer.")
        return

    # Secure Execution
    try:
        value = int(input_value)
        offset = 1000
        result = value + offset
        print(f"Result: {result}")
    except ValueError:
        print("Error: An unexpected error occurred during execution.")

if __name__ == "__main__":
    main()