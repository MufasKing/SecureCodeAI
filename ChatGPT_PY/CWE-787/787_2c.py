def main():
    # Allocate two chunks of memory, each of size 10
    chunk1 = bytearray(10)  # First chunk
    chunk2 = bytearray(10)  # Second chunk

    # Fill chunk1 with some data
    for i in range(len(chunk1)):
        chunk1[i] = i

    # Copy the contents of chunk1 into chunk2
    chunk2[:] = chunk1

    # Print the contents of chunk2 to verify the copy
    print("Contents of chunk2 after copying from chunk1:", list(chunk2))

    # Freeing memory in Python is handled by garbage collection
    # Here, we can simply delete the references to simulate "freeing" memory
    del chunk1
    del chunk2

    # After deletion, the memory should be automatically reclaimed by Python's garbage collector
    # You can run `gc.collect()` if you want to force garbage collection, but it's usually not necessary

if __name__ == "__main__":
    main()
