import ctypes

buffer_size = 100

# Allocate the buffer on the stack using ctypes
buffer = ctypes.c_buffer(buffer_size)

# Overwrite all values in the buffer with 'A'
for i in range(buffer_size):
    buffer[i] = ord('A')

# Set the buffer to be invalid after it goes out of scope
buffer.set_invalid()

print(buffer)