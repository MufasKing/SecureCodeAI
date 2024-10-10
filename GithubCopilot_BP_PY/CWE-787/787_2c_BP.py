import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, ctypes.sizeof(chunk1))

# Zero the memory of the first chunk before freeing (for security)
ctypes.memset(chunk1, 0, ctypes.sizeof(chunk1))

# Free the first chunk by dereferencing
del chunk1

# Zero the memory of the second chunk before freeing (for security)
ctypes.memset(chunk2, 0, ctypes.sizeof(chunk2))

# Free the second chunk by dereferencing
del chunk2