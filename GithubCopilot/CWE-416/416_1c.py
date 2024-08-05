# Allocate a buffer of size buffer_size
buffer_size = 1024  # Example buffer size
buffer = bytearray(buffer_size)

# Free the buffer in a loop
for _ in range(1):
    buffer = None  # Free the buffer by setting it to None