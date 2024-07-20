import ctypes

# Allocate two chunks of memory, each of size 10
size = 10
chunk1 = (ctypes.c_char * size)()
chunk2 = (ctypes.c_char * size)()

# Initialize the first chunk with some data
for i in range(size):
    chunk1[i] = ctypes.c_char(b'A' + i)  # Fill with ASCII characters starting from 'A'

# Copy contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, size)

# Print the contents of the second chunk
print(bytes(chunk2).decode('utf-8'))
