import ctypes

buffer_size = 1024
buffer = (ctypes.c_char * buffer_size)()
for i in range(buffer_size):
    buffer[i] = 'A'

print(buffer)