import ctypes
import copy

def allocate_memory(size):
    """Allocate memory and return a pointer to it."""
    return (ctypes.c_int * size)()

def copy_memory(source, destination, size):
    """Copy contents from source to destination."""
    ctypes.memmove(destination, source, ctypes.sizeof(source[0]) * size)

def print_memory(chunk, size):
    """Print the contents of the memory chunk."""
    for i in range(size):
        print(chunk[i], end=' ')
    print()

def free_memory(chunk):
    """Free the allocated memory. In Python, this is handled by garbage collection."""
    del chunk

def main():
    try:
        # Allocate two chunks of memory each of size 10
        chunk1 = allocate_memory(10)
        chunk2 = allocate_memory(10)
        
        # Initialize chunk1 with some values for demonstration
        for i in range(10):
            chunk1[i] = i + 1
        
        # Copy the contents of the first chunk into the second chunk
        copy_memory(chunk1, chunk2, 10)
        
        # Print the contents of the second chunk
        print("Contents of chunk2 after copying from chunk1:")
        print_memory(chunk2, 10)
        
        # Free the memory allocated to the first chunk
        free_memory(chunk1)
        
        # Attempt to print the contents of the second chunk after freeing the first chunk
        print("Contents of chunk2 after freeing chunk1 (should be unchanged):")
        print_memory(chunk2, 10)
        
        # Free the memory allocated to the second chunk
        free_memory(chunk2)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()