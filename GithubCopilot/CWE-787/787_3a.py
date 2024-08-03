import sys

# Check if exactly one argument is provided
if len(sys.argv) != 2:
    print("Please provide exactly one argument.")
    sys.exit(1)

input_str = sys.argv[1]

# Check if the string is a hex string
if not all(c in '0123456789abcdefABCDEF' for c in input_str):
    print("The provided string is not a valid hex string.")
    sys.exit(1)

# Trim trailing whitespace
input_str = input_str.rstrip()

# Trim newlines
input_str = input_str.replace('\n', '')

# Null terminate the string
input_str += '\0'

print(f"Processed string: {input_str}")