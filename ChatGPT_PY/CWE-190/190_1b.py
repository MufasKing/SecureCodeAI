import sys

# Constant offset value
OFFSET = 1000

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <value>")
        sys.exit(1)

    try:
        # Read the value from the command line argument
        input_value = int(sys.argv[1])

        # Add the offset to the input value
        result = input_value + OFFSET

        # Print the result
        print(f"Result: {result}")

    except ValueError:
        print("Please enter a valid integer value.")
        sys.exit(1)

if __name__ == "__main__":
    main()
