def allocate_and_free(buffer_size, iterations):
    # Allocate a buffer of the specified size
    for _ in range(iterations):
        # Create a buffer of the specified size
        buffer = bytearray(buffer_size)
        # Do something with the buffer if needed
        print(f"Allocated buffer of size {buffer_size}")

        # Explicitly delete the buffer to simulate freeing
        del buffer
        print("Buffer freed")

# Example usage
buffer_size = 1024  # Size of the buffer in bytes
iterations = 5      # Number of times to allocate and free the buffer

allocate_and_free(buffer_size, iterations)
