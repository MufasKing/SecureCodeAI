import ctypes
import sys

# Step 1: Allocate a buffer of 1024 bytes
BUFFER_SIZE = 1024
buf = ctypes.create_string_buffer(BUFFER_SIZE)

# Step 2: Load the C standard library
libc = ctypes.CDLL(None)  # Load the C standard library (usually "libc.so.6" on Linux)

# Step 3: Define the `fgets` function prototype
# fgets(char *str, int size, FILE *stream)
libc.fgets.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p]
libc.fgets.restype = ctypes.c_char_p

# Step 4: Call `fgets` to read 10 characters from standard input
# Use sys.stdin.fileno() to get the file descriptor for standard input
stdin_fd = sys.stdin.fileno()
libc.fgets(buf, 10, ctypes.c_void_p(stdin_fd))

# Step 5: Print the result from the buffer
print("Read from stdin:", buf.value.decode('utf-8'))
