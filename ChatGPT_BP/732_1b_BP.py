import os
import errno

def write_to_file(file_path, content):
    try:
        # Define the flags for opening the file
        flags = os.O_WRONLY | os.O_CREAT
        # Define the mode (permissions) for the new file
        mode = os.S_IRUSR | os.S_IWUSR

        # Open the file descriptor with specified flags and mode
        fd = os.open(file_path, flags, mode)

        try:
            # Write the content to the file
            os.write(fd, content.encode())
        finally:
            # Ensure the file descriptor is closed properly
            os.close(fd)
            
    except OSError as e:
        # Handle specific errors
        if e.errno == errno.EACCES:
            print("Permission denied: unable to write to the file.")
        elif e.errno == errno.ENOENT:
            print("No such file or directory.")
        else:
            print(f"An unexpected error occurred: {e}")

# Define the path and the content to write
file_path = "important_config"
content = "important_config"

# Call the function to write to the file
write_to_file(file_path, content)