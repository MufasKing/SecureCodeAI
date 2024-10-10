import ctypes

import sys



def scan(prompt):

    """

    Reads in a string from the standard input until a newline character is seen.

    The newline character is not stored in the buffer.

    Performs secure input handling, prompt flushing, error handling, and string decoding.

    Reads in at most 1023 characters due to buffer size limitation.

    """

    # Prompt user

    sys.stdout.write(prompt)

    sys.stdout.flush()



    # Create a buffer for the input

    buffer_size = 1024

    buffer = ctypes.create_string_buffer(buffer_size)



    try:

        # Read from stdin (fd = 0) using ctypes

        libc = ctypes.CDLL("libc.so.6")

        read = libc.read

        read.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t]

        read.restype = ctypes.c_ssize_t



        # Perform the read operation

        num_chars_read = read(0, buffer, buffer_size - 1)  # Leave space for null terminator



        if num_chars_read > 0:

            # Successfully read, now decode and strip newline if present

            input_str = buffer.value.decode('utf-8')

            if input_str.endswith(''):

                input_str = input_str[:-1]

            return input_str

        else:

            # Handle error or EOF

            if num_chars_read == 0:

                print("EOF encountered. No input read.")

            else:

                print("Error reading input.")

            return None

    except Exception as e:

        print(f"An error occurred: {e}")

        return None



# Example usage

if __name__ == "__main__":

    user_input = scan("Enter input: ")

    if user_input is not None:

        print(f"You entered: {user_input}")

    else:

        print("Failed to read input.")