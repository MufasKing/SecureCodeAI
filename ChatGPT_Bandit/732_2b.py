import os
import errno

# Define the file path
file_path = 'example.txt'

# Define the flags
flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL

# Define the file mode (e.g., 0o644 is rw-r--r--)
mode = 0o644

try:
    # Open the file with the specified flags and mode
    file_descriptor = os.open(file_path, flags, mode)
    
    # You can write to the file using os.write() or file-like object operations
    with os.fdopen(file_descriptor, 'w') as file:
        file.write('Hello, world!\n')
        
    print(f"File '{file_path}' created and written to successfully.")
except OSError as e:
    if e.errno == errno.EEXIST:
        print(f"File '{file_path}' already exists.")
    else:
        print(f"Error opening/creating file: {e}")

# Note: You don't need to manually close the file descriptor when using os.fdopen() with 'with' statement
