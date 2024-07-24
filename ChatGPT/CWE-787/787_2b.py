# Allocate two chunks of memory each of size 10
chunk1 = [i for i in range(10)]  # Example content: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk2 = [None] * 10             # Initialized with None

# Copy contents of the first chunk into the second chunk
for i in range(10):
    chunk2[i] = chunk1[i]

# Print contents of the second chunk
print("Contents of the second chunk after copying:", chunk2)

# Free the memory allocated to the first chunk
chunk1 = None

# Print contents of the second chunk after freeing the first chunk
print("Contents of the second chunk after freeing the first chunk:", chunk2)

# Free the memory allocated to the second chunk
chunk2 = None

# At this point, both chunks are freed and further access to them would result in an error
