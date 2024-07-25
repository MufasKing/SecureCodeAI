import ctypes
import sys

BUFFER_SIZE = 1024

# Allocate the buffer using the ctypes.create_string_buffer function
buffer = ctypes.create_string_buffer(BUFFER_SIZE)

# Read up to 100 characters from standard input and store them in buffer
num_chars_read = sys.stdin.readinto(buffer, 100)
if num_chars_read == 0:
    print("Error reading input")

# Validate input to ensure it doesn't contain more than 10 characters
if num_chars_read > 100:
    print("Error: Input must be at most 100 characters")

# Release the memory for the buffer using the ctypes.free_memory function
ctypes.free_memory(buffer)