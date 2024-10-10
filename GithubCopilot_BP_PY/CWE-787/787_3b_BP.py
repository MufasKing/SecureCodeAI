import sys

# First, check if the number of arguments is exactly 2 (the script name and one user-provided argument)
if len(sys.argv) != 2:
    print("Error: Please provide exactly one argument.")
    sys.exit(1)  # Exit the program with an error code

# Second, safely get the user-provided argument
try:
    input_argument = sys.argv[1]
except IndexError:
    # This block is technically redundant due to the earlier check, but included for completeness
    print("Error: No argument provided.")
    sys.exit(1)

# Third, print the original argument
print("Original argument:", input_argument)

# Fourth, trim the trailing whitespace from the argument
trimmed_argument = input_argument.rstrip()

# Fifth, print the trimmed argument
print("Trimmed argument:", trimmed_argument)

# Sixth, exit the program successfully
sys.exit(0)