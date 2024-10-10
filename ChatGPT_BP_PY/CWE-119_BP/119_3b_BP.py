import sys

def atoi(s):
    """
    Converts a string to an integer.
    """
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Invalid integer value: '{s}'")

def main(argv):
    """
    Main function to handle command-line arguments.
    """
    argc = len(argv)

    # Argument count validation
    if argc < 2:
        print("Error: No arguments provided.")
        print("Usage: python script.py <arg1> <arg2> ... <argN>")
        return 1

    # Iterate over arguments (excluding the script name itself)
    for i in range(1, argc):
        arg = argv[i]
        try:
            sanitized_arg = arg.strip()
            if not sanitized_arg:
                print(f"Error: Argument {i} is empty or only contains whitespace.")
                continue
            
            # Convert to integer
            num = atoi(sanitized_arg)
            print(f"Argument {i}: {sanitized_arg} -> {num}")

        except ValueError as e:
            print(f"Error processing argument {i}: {e}")

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))