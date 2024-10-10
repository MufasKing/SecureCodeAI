import os
import tempfile

# Define the string to be written to the file
important_config = "configuration data"

try:
    # Create a temporary file using a context manager to ensure it's properly closed
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp_file:
        # Get the temporary file's name
        tmp_file_name = tmp_file.name
        
        # Open the temporary file with read and write permissions (O_RDWR)
        # and create it if it doesn't exist (O_CREAT)
        # File permissions are set to 0700 (read, write, and execute for the owner only)
        fd = os.open(tmp_file_name, os.O_RDWR | os.O_CREAT, 0o700)
        
        # Convert the file descriptor to a file object
        with os.fdopen(fd, 'w') as file_obj:
            # Write the important configuration data to the file
            file_obj.write(important_config)
            # Ensure all data is written to disk
            file_obj.flush()
            os.fsync(file_obj.fileno())
            
        print(f"Configuration data written to temporary file: {tmp_file_name}")
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Securely delete the temporary file if it exists
    if 'tmp_file_name' in locals() or 'tmp_file_name' in globals():
        os.remove(tmp_file_name)
        print(f"Temporary file {tmp_file_name} has been securely deleted.")