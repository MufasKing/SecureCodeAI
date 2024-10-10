import ctypes
import sys

# Load the shared library
libscan = ctypes.CDLL('./libscan.so')

# Define the scan function's signature
# int scan(char *buffer)
libscan.scan.argtypes = [ctypes.c_char_p]
libscan.scan.restype = ctypes.c_int

def scan():
    # Create a buffer to hold the input string
    buffer = ctypes.create_string_buffer(1024)
    
    # Call the C function
    count = libscan.scan(buffer)
    
    # Decode the buffer to a Python string (buffer is null-terminated)
    input_string = buffer.value.decode('utf-8')
    
    # Print the result and return the count
    print("Read string:", input_string)
    print("Number of characters read:", count)
    
    return count

if __name__ == '__main__':
    scan()
