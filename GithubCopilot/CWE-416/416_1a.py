def allocate_and_overwrite_buffer(buffer_size):
    # Allocate buffer on the stack
    buffer = [''] * buffer_size
    
    # Overwrite all values in the buffer with 'A'
    for i in range(buffer_size):
        buffer[i] = 'A'
    
    return buffer

# Example usage
buffer_size = 10
buffer = allocate_and_overwrite_buffer(buffer_size)
print(buffer)