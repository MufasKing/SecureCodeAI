import sys

def validate_input(input_str):
    """
    Validate the command-line argument to ensure it meets the criteria.
    Raises ValueError if the input is not valid.
    """
    if not input_str:
        raise ValueError("Input cannot be empty")
    if len(sys.argv) != 2:
        raise ValueError("Exactly one argument is required.")

def sanitize_input(input_str):
    """
    Sanitize the input by trimming trailing whitespace characters.
    """
    return input_str.rstrip()

def execute_and_print(sanitized_input):
    """
    Execute the core functionality and print the sanitized input.
    """
    print(f"Command-line argument: {sanitized_input}")

def main():
    """
    Main function to orchestrate the validation, sanitization, and execution.
    """
    try:
        validate_input(sys.argv[1])
        sanitized_input = sanitize_input(sys.argv[1])
        execute_and_print(sanitized_input)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()