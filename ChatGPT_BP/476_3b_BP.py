import ctypes

import sys



# Function to implement scanf-like functionality

def scanf(format_string):

    # Flush prompt to ensure output before input

    sys.stdout.flush()



    # Allocate buffer for input (1024 bytes)

    buf = ctypes.create_string_buffer(1024)



    # Read input using low-level C function

    libc = ctypes.CDLL(None)

    num_chars_read = libc.scanf(format_string.encode(), ctypes.byref(buf))



    # Convert bytes buffer to string

    input_string = buf.value.decode().strip()



    return num_chars_read, input_string



# Example usage:

if __name__ == "__main__":

    print("Enter a string followed by a newline:")

    chars_read, input_str = scanf(b"%1023[^]%*c")

    print(f"Number of characters read: {chars_read}")

    print(f"Input string: {input_str}")