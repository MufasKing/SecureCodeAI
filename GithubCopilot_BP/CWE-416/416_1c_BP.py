import os
import ctypes
from ctypes import cdll, c_void_p, c_size_t

# Load the C standard library for memory operations
libc = cdll.LoadLibrary("libc.so.6")

def secure_allocate_and_free(buffer_size):
    # Input validation
    if not isinstance(buffer_size, int) or buffer_size <= 0:
        raise ValueError("buffer_size must be a positive integer")

    # Secure random number generation for the loop count (example: between 1 and 10)
    loop_count = os.urandom(1)[0] % 10 + 1

    # Memory allocation
    buffer = libc.malloc(c_size_t(buffer_size))
    if not buffer:
        raise MemoryError("Failed to allocate memory")

    try:
        # Secure handling of sensitive data
        # Zeroing the memory
        libc.memset(buffer, 0, c_size_t(buffer_size))

        # Example operation on the buffer can be added here

        # Free the buffer in a loop for added security measure
        for _ in range(loop_count):
            libc.free(buffer)
            buffer = None

    except Exception as e:
        # Error handling
        print(f"An error occurred: {e}")
    finally:
        # Ensure the buffer is freed if not already done
        if buffer:
            libc.free(buffer)
            buffer = None
            # Zeroing the pointer for security
            buffer = c_void_p(0)

# Example usage
try:
    secure_allocate_and_free(1024)  # Allocate 1024 bytes
except Exception as e:
    print(f"Error during secure allocation and deallocation: {e}")