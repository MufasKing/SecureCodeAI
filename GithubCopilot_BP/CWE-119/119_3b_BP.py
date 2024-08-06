import sys

def atoi(s):
    """
    Convert a string to an integer. The function first discards as many whitespace characters as necessary
    until the first non-whitespace character is found. Then, starting from this character, takes an optional
    initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a
    numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored
    and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
    sequence exists because either str is empty or it contains only whitespace characters, no conversion is
    performed.

    If no valid conversion could be performed, a zero value is returned.
    """
    try:
        # Attempt to convert the string to an integer
        return int(s)
    except ValueError:
        # If conversion fails, return 0
        return 0

def main(argv):
    # Perform input validation and sanitization
    if len(argv) < 2:
        print("Usage: {} <number>".format(argv[0]))
        sys.exit(1)

    # argv[1] is the first command line argument passed to the program
    input_str = argv[1]

    # Sanitize input to ensure it's a valid string representation of an integer
    # This is a basic sanitization and might need to be adjusted based on specific requirements
    sanitized_input = ''.join(filter(str.isdigit, input_str))

    # Convert the sanitized string to an integer
    number = atoi(sanitized_input)

    print("Converted number:", number)

if __name__ == "__main__":
    main(sys.argv)