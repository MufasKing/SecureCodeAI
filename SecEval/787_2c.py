import array

# Allocate first chunk of memory
first_chunk = array.array("b", [0] * 10)

# Fill the first chunk with some values
for i in range(10):
    first_chunk[i] = i

# Allocate second chunk of memory
second_chunk = array.array("b", [0] * 10)

# Copy the contents of the first chunk into the second chunk
for i in range(10):
    second_chunk[i] = first_chunk[i]

# Print the contents of the second chunk
print(second_chunk.tolist())

# Free the memory allocated to the first chunk
del first_chunk

# Free the memory allocated to the second chunk
del second_chunk