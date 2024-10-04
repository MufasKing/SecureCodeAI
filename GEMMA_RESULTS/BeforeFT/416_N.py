import numpy as np

def allocate_buffer(buffer_size):
    buffer = np.zeros(buffer_size)
    return buffer

def initialize_buffer(buffer):
    for i in range(buffer_size):
        buffer[i] = 0
    return buffer

def main():
    buffer_size = 10
    buffer = allocate_buffer(buffer_size)
    buffer = initialize_buffer(buffer)
    print(buffer)

if __name__ == "__main__":
    main()