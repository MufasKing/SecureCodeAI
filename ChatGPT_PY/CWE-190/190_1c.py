import sys

def main():
    # Check if the argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        return 1

    try:
        # Read the input value from the command line
        input_value = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        return 1

    # Add 1000 to the input value
    result = input_value + 1000

    # Print the result
    print(result)

    # Return 0
    return 0

if __name__ == "__main__":
    sys.exit(main())
