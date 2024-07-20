import os
import tempfile
import errno

def create_and_write_secure_file():
    # Create a temporary file
    fd, temp_path = tempfile.mkstemp()
    
    try:
        # Set the permissions to 0700
        os.chmod(temp_path, 0o700)
        
        # Write the string "important_config" to the file
        os.write(fd, b"important_config")
        
    except OSError as e:
        if e.errno == errno.EACCES:
            print("Permission error while accessing the file.")
        elif e.errno == errno.EIO:
            print("I/O error while accessing the file.")
        else:
            print(f"An unexpected error occurred: {e}")
    finally:
        # Always close the file descriptor
        os.close(fd)
        
        # Optionally, you can remove the temporary file after use
        os.remove(temp_path)

# Call the function to create and write to the secure file
create_and_write_secure_file()