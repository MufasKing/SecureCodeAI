import sys

def read_input():
    # Initialize a counter for the number of characters read
    char_count = 0

    # Create an array to store the characters read from the input
    chars = bytearray()

    # Read characters from the standard input until a newline character is encountered
    try:
        while True:
            # Read a single byte (character) from the standard input
            byte = sys.stdin.read(1)
            
            # Check if the byte is a newline character (, ASCII code 10)
            if ord(byte) == 10:
                # The newline character has been encountered, break the loop
                break
            
            # If the byte is not a newline, add it to the array of characters
            chars.append(byte)
            
            # Increment the character count
            char_count += 1

    except UnicodeDecodeError:
        # Handle UnicodeDecodeError in case the input stream is not encoded in UTF-8
        print("Error: The input stream is not encoded in UTF-8.")
        sys.exit(1)

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Error: {str(e)}")
        sys.exit(1)

    # Return the number of characters read (excluding the newline character, if present)
    return char_count

# Read input and print the number of characters read
num_chars = read_input()
print(f"Number of characters read: {num_chars}")