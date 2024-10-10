import sys

def main():
    # Check to ensure exactly one argument is provided
    if len(sys.argv) != 2:
        print("Error: Exactly one argument is required.")
        sys.exit(1)

    # Get the argument from the command line
    user_input = sys.argv[1]

    # Print the argument
    print(f"Original input: '{user_input}'")

    # Trim the trailing whitespace from the argument
    trimmed_input = user_input.rstrip()

    # Print the trimmed argument
    print(f"Trimmed input: '{trimmed_input}'")

    # Exit the program
    sys.exit(0)

if __name__ == "__main__":
    main()