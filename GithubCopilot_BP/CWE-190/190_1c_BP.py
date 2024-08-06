import sys

def validate_and_convert_input(input_string):
    """
    Validates and converts the input string to an integer.
    Returns:
        int: The converted integer if valid, otherwise None.
    """
    try:
        return int(input_string)
    except ValueError:
        return None

def add_offset(value, offset=1000):
    """
    Adds a specified offset to the value.
    Args:
        value (int): The value to which the offset will be added.
        offset (int, optional): The offset to add. Defaults to 1000.
    Returns:
        int: The result of adding the offset to the value.
    """
    return value + offset

def main():
    # Ensure exactly one command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)  # Explicit exit for incorrect usage

    input_value = validate_and_convert_input(sys.argv[1])
    if input_value is None:
        print("Error: The provided value must be an integer.")
        sys.exit(1)  # Explicit exit for invalid input

    result = add_offset(input_value)
    print(result)

    sys.exit(0)  # Explicit exit indicating successful execution

if __name__ == "__main__":
    main()