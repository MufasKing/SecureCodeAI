import sys

def is_hex_string(s):
    # Check if the string is a valid hexadecimal string
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def main():
    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <hex_string>")
        sys.exit(1)
    
    hex_string = sys.argv[1]
    
    # Check if the string is a valid hexadecimal string
    if not is_hex_string(hex_string):
        print("Error: The argument must be a valid hexadecimal string.")
        sys.exit(1)
    
    # Trim trailing whitespace
    trimmed_hex_string = hex_string.rstrip()
    
    # Trim newlines
    trimmed_hex_string = trimmed_hex_string.rstrip('\n')
    
    # Null-terminate the string (In Python, this is just adding a '\0' at the end)
    null_terminated_string = trimmed_hex_string + '\0'
    
    # Print the null-terminated string (For demonstration purposes)
    print("Null-terminated string:", repr(null_terminated_string))

if __name__ == "__main__":
    main()
