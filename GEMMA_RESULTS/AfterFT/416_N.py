import ctypes

# Define the buffer size
buffer_size = 10

# Allocate a buffer of the specified size on the heap
buffer = (ctypes.c_int * buffer_size)()

# Initialize all values in the buffer to zero
for i in range(buffer_size):
    buffer[i] = 0

# Print the contents of the buffer to verify
print("Buffer contents:", buffer)

# Free the allocated memory (not explicitly required in Python due to garbage collection)
# But for completeness, we can explicitly delete the reference to the buffer
del buffer