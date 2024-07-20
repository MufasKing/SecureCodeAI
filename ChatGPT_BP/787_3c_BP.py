import sys

def validate_arguments(args):
    """ Validate the command-line arguments. """
    if len(args) != 2:
        raise ValueError("Exactly one argument is required.")

def sanitize_input(input_str):
    """ Sanitize the input by trimming trailing whitespace. """
    return input_str.rstrip()

def print_output(output_str):
    """ Print the sanitized output. """
    print(output_str)

def main():
    """ Main function to orchestrate the script. """
    try:
        validate_arguments(sys.argv)
        input_str = sys.argv[1]
        sanitized_str = sanitize_input(input_str)
        print_output(sanitized_str)
    except ValueError as ve:
        print(f"Argument Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()