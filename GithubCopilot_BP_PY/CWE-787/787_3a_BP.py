import sys



# Handling command-line arguments

if len(sys.argv) != 2:

    print("Error: Please provide exactly one argument.")

    sys.exit(1)



input_string = sys.argv[1]



# Input Validation for hex string

if not all(c in "0123456789abcdefABCDEF" for c in input_string):

    print("Error: The provided string is not a valid hex string.")

    sys.exit(1)



# Input Sanitization

# Trim trailing whitespace

input_string = input_string.rstrip()



# Trim newlines

input_string = input_string.replace("", "")



# Error Handling is integrated within the checks for command-line arguments and hex string validation



# Null terminate the string

input_string += ""



print("Processed string:", input_string)