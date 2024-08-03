import sys

# Check if exactly one argument is provided
if len(sys.argv) != 2:
    print("Error: Exactly one argument is required.")
    sys.exit(1)

# Get the argument from the command line
input = sys.argv[1]

# Print the argument
print(input)

# Trim the trailing whitespace from the argument
input = input.rstrip()

# Print the argument again
print(input)

# Exit the program
sys.exit(0)