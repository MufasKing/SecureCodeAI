import sys

def validate_and_convert_input(input_str, minimum, maximum):
    """
    Validates and converts the input string to an integer within the specified range.
    If the input is not a valid integer or it's out of range, the function raises a ValueError.
    
    Args:
        input_str (str): The input string to be validated and converted.
        minimum (int): The minimum acceptable value for the input.
        maximum (int): The maximum acceptable value for the input.
    
    Returns:
        int: The converted integer within the specified range.
    """
    try:
        value = int(input_str)
        if value < minimum or value > maximum:
            raise ValueError(f"Input value '{input_str}' is out of range (min: {minimum}, max: {maximum})")
    except ValueError as e:
        raise ValueError(f"Invalid input '{input_str}'. {e}")
    
    return value

def add_two_numbers(a, b):
    """
    Adds two integers and returns the result.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The sum of the two integers.
    """
    return a + b

def main():
    """
    Main function to handle the addition of two integers.
    """
    # Define the minimum and maximum acceptable values for the inputs
    MIN = 0  # For example, let's consider only positive integers
    MAX = 100  # For example, let's consider a small range for simplicity

    # Check if the required number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <first_number> <second_number>")
        sys.exit(1)

    # Validate and convert the inputs
    try:
        num1 = validate_and_convert_input(sys.argv[1], MIN, MAX)
        num2 = validate_and_convert_input(sys.argv[2], MIN, MAX)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Perform the addition
    result = add_two_numbers(num1, num2)

    # Print the result
    print(f"The result of adding {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()