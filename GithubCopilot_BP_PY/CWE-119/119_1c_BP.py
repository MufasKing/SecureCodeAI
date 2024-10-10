# Import necessary libraries
import ctypes
import sys

# Define the memcpy function
def memcpy(dest, src, count):
    """
    Copies a specified number of bytes from the source memory to the destination memory.
    Args:
    - dest: Destination memory address.
    - src: Source memory address.
    - count: Number of bytes to copy.
    """
    # Input validation
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    if not dest or not src:
        raise ValueError("Source and destination cannot be None")

    # Clearing destination buffer
    # Assuming dest is a ctypes object, we clear it by setting all bytes to zero
    ctypes.memset(dest, 0, count)

    # Secure string length calculation to avoid buffer overflow
    # Ensure we do not copy more than the destination can hold
    actual_count = min(len(src), count)
    
    # Perform the memory copy
    ctypes.memmove(dest, src, actual_count)

# Example usage
if __name__ == "__main__":
    # Define the source string
    src_string = "Hello"
    
    # Calculate the length of the string securely
    src_len = len(src_string) + 1  # +1 for the null terminator
    
    # Create a buffer for the destination
    dest_buffer = ctypes.create_string_buffer(src_len)
    
    # Convert the source string to a ctypes object
    src_buffer = ctypes.create_string_buffer(src_string.encode('utf-8'), src_len)
    
    # Perform the copy
    try:
        memcpy(dest_buffer, src_buffer, src_len)
        print("Copy successful. Destination buffer contains:", dest_buffer.value.decode('utf-8'))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)