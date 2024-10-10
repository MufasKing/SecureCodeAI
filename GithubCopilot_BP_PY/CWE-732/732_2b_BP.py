import os

def secure_file_open(filename):
    # Define the flags for open()
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL

    # Define the mode for the file (rw-r--r--)
    mode = 0o644

    try:
        # Check if the file exists to avoid using O_EXCL unnecessarily
        if not os.path.exists(filename):
            # Open the file with the specified flags and mode
            file_descriptor = os.open(filename, flags, mode)
            # Convert the file descriptor to a file object
            with os.fdopen(file_descriptor, 'w') as file:
                # File is ready for writing
                print(f"File {filename} opened successfully for writing.")
                # Perform file operations here
        else:
            print(f"File {filename} already exists.")
    except OSError as e:
        # Handle exceptions, such as permission issues or file exists (if O_EXCL is used and file exists)
        print(f"Error opening file {filename}: {e}")

# Example usage
secure_file_open('example.txt')