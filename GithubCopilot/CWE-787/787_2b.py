import ctypes

# Allocate two chunks of memory each of size 10
chunk1 = (ctypes.c_char * 10)()
chunk2 = (ctypes.c_char * 10)()

# Fill the first chunk with some data
for i in range(10):
    chunk1[i] = bytes([65 + i])  # ASCII values from 'A' to 'J'

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(chunk2, chunk1, 10)

# Print the contents of the second chunk
print("Contents of the second chunk after copy:", bytes(chunk2).decode('utf-8'))

# Free the memory allocated to the first chunk
del chunk1

# Print the contents of the second chunk
print("Contents of the second chunk after freeing the first chunk:", bytes(chunk2).decode('utf-8'))

# Free the memory allocated to the second chunk
del chunk2