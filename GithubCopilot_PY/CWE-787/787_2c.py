import ctypes

# Allocate two chunks of memory, each of size 10
chunk1 = ctypes.create_string_buffer(10)
chunk2 = ctypes.create_string_buffer(10)

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Free the first chunk (not necessary in Python, but for demonstration)
del chunk1

# Free the second chunk (not necessary in Python, but for demonstration)
del chunk2