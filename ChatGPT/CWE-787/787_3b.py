import sys

# Check if exactly one argument is provided
if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument.")
    sys.exit(1)

# Get the argument from the command line
input_arg = sys.argv[1]

# Print the argument
print("Original argument:", input_arg)

# Trim trailing whitespace from the argument
trimmed_arg = input_arg.rstrip()

# Print the trimmed argument
print("Trimmed argument:", trimmed_arg)

# Exit the program
sys.exit(0)
