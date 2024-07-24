import ctypes

# Allocate two chunks of memory, each of size 10
size = 10
chunk1 = (ctypes.c_char * size)()
chunk2 = (ctypes.c_char * size)()

# Initialize the first chunk with some data
for i in range(size):
    chunk1[i] = b'a'[0] + i

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, size)

# Print contents of the chunks to verify the copy
print("Chunk 1:", bytes(chunk1))
print("Chunk 2:", bytes(chunk2))

# Zeroing the memory of the first chunk
ctypes.memset(chunk1, 0, size)

# Freeing the first chunk (not explicitly necessary in Python, but for completeness)
del chunk1

# Freeing the second chunk (not explicitly necessary in Python, but for completeness)
del chunk2