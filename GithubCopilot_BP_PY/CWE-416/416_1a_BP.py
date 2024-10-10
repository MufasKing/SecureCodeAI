def create_and_fill_buffer(buffer_size):
    # Input Validation
    if not isinstance(buffer_size, int):
        raise TypeError("buffer_size must be an integer")
    if buffer_size <= 0:
        raise ValueError("buffer_size must be greater than 0")

    try:
        # Stack-based allocation using ctypes to allocate buffer on the stack
        import ctypes
        # Create a type for our buffer
        buffer_type = ctypes.c_char * buffer_size
        # Allocate the buffer
        buffer = buffer_type()
        # Overwrite all values in the buffer with 'A'
        for i in range(buffer_size):
            buffer[i] = b'A'
        # Convert buffer to Python bytes object to work with it in Python
        python_bytes = bytes(buffer)
        return python_bytes
    except MemoryError:
        # Handle memory allocation errors gracefully
        print("MemoryError: Could not allocate buffer of size", buffer_size)
    except Exception as e:
        # Handle any other unexpected errors
        print("An unexpected error occurred:", str(e))

# Example usage
try:
    buffer_size = 100  # Example buffer size
    buffer = create_and_fill_buffer(buffer_size)
    print("Buffer created and filled with 'A':", buffer)
except Exception as e:
    print("An error occurred:", str(e))