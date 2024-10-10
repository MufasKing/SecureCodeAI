import ctypes
import sys

# Constants
BUFFER_SIZE = 1024
READ_SIZE = 100

def allocate_buffer(size):
    """Allocate a buffer of the given size using ctypes."""
    return ctypes.create_string_buffer(size)

def read_input_into_buffer(buffer, size):
    """Read up to 'size' characters from stdin into the provided buffer."""
    # Read input from stdin
    input_data = sys.stdin.read(size)
    # Ensure the data fits into the buffer and null-terminate it
    buffer[:size] = input_data.encode('utf-8')[:size]
    buffer[size - 1] = 0  # Null-terminate the string

def main():
    # Allocate two buffers of 1024 bytes each
    buf = allocate_buffer(BUFFER_SIZE)
    buf1 = allocate_buffer(BUFFER_SIZE)

    # Read 100 characters from stdin into buf
    print("Please enter at least 100 characters:")
    read_input_into_buffer(buf, READ_SIZE)
    
    # Read another 100 characters from stdin into buf1
    print("Please enter another 100 characters:")
    read_input_into_buffer(buf1, READ_SIZE)

    # Print the contents of buffers for demonstration
    print("Buffer 1 contents:")
    print(buf.value.decode('utf-8'))

    print("Buffer 2 contents:")
    print(buf1.value.decode('utf-8'))

if __name__ == "__main__":
    main()
