import sys

def add_1000(value):
    """
    Add 1000 to the input value.
    
    Parameters:
    value (int): The input value to which 1000 will be added.
    
    Returns:
    int: The result of adding 1000 to the input value.
    """
    return value + 1000

def validate_input(value):
    """
    Validate the input to ensure it is an integer.
    
    Parameters:
    value (str): The input value as a string.
    
    Returns:
    int: The input value converted to an integer.
    
    Raises:
    ValueError: If the input value cannot be converted to an integer.
    """
    try:
        return int(value)
    except ValueError as e:
        raise ValueError(f"Invalid input '{value}'. Please enter a valid integer.") from e

def main():
    """
    Main function to handle the flow of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <integer>")
        sys.exit(1)

    input_value = sys.argv[1]
    
    try:
        validated_value = validate_input(input_value)
        result = add_1000(validated_value)
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()