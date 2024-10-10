def memcpy(dest, src, n):
    for i in range(n):
        dest[i] = src[i]

def strlen(s):
    length = 0
    for char in s:
        length += 1
    return length

# Source string
source = "Hello"

# Create a buffer with the same length as the source string
buffer = [''] * strlen(source)

# Copy the string "Hello" to the buffer
memcpy(buffer, source, strlen(source))

# Convert buffer list back to string
copied_string = ''.join(buffer)

print(copied_string)  # Output should be "Hello"