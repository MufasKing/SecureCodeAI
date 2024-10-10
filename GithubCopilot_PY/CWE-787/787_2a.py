import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Fill the first chunk with some data
data = b'abcdefghij'
for i in range(10):
    chunk1[i] = data[i]

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Print the contents of the second chunk
print(bytes(chunk2).decode('utf-8'))