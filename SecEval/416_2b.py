import hashlib

# The path to the file to read
file_path = "path/to/file.txt"

# Open the file for reading
with open(file_path, "rb") as f:
    # Read the contents of the file into a buffer
    buffer = f.read()


    # Calculate the checksum of the buffer
    checksum = hashlib.md5(buffer).hexdigest()
    
    # Check if the buffer is empty
    if len(buffer) == 0:
        print("Buffer is empty")
    else:
        # Save the number of bytes read and the checksum to another file
        with open("checksum_result.txt", "w") as f:
            f.write("Number of bytes read: {}
".format(len(buffer)))
            f.write("Checksum: {}".format(checksum))