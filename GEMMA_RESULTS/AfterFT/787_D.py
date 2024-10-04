import ctypes

# Input size
SIZE = 10

# Allocate two chunks of memory each of size 10
array_1 = (ctypes.c_char * SIZE)()
array_2 = (ctypes.c_char * SIZE)()

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(array_2, array_1, SIZE * ctypes.sizeof(array_1[0]))

# Print the contents of the second chunk
print("Contents of the second chunk:", ''.join(map(chr, array_2)))

# Secure disposal of sensitive data
# Zeroing the memory to prevent memory leaks and sensitive data exposure
ctypes.memset(array_1, 0, SIZE * ctypes.sizeof(array_1[0]))
ctypes.memset(array_2, 0, SIZE * ctypes.sizeof(array_2[0]))

# Secure disposal of memory pointers
array_1 = None
array_2 = None