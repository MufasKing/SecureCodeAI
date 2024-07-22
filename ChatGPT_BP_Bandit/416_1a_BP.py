def allocate_and_fill_buffer(buffer_size):
    import ctypes

    # Input validation: Ensure buffer_size is a positive integer
    if not isinstance(buffer_size, int) or buffer_size <= 0:
        raise ValueError("buffer_size must be a positive integer")
    
    try:
        # Allocate a buffer on the stack
        buffer = (ctypes.c_char * buffer_size)()
        
        # Fill the buffer with 'A' (ASCII value 65)
        for i in range(buffer_size):
            buffer[i] = b'A'
        
        # Print the buffer contents for verification
        print("Buffer contents:", bytes(buffer))
        return bytes(buffer)  # Return the buffer as bytes object
    except Exception as e:
        # Error handling: Print error message and re-raise the exception
        print(f"An error occurred: {e}")
        raise

# Example usage
try:
    buffer_size = 10  # Define the buffer size
    buffer = allocate_and_fill_buffer(buffer_size)
    print("Buffer allocated and filled successfully.")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Exception: {e}")