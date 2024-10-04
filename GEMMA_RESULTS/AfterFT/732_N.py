import os

def create_or_open_file(file_path, truncate=False, exclusive=False):
    # Define the flags based on the input parameters
    flags = os.O_WRONLY
    if truncate:
        flags |= os.O_TRUNC
    if exclusive:
        flags |= os.O_EXCL
    
    try:
        # Open the file with the specified flags
        fd = os.open(file_path, flags | os.O_CREAT, 0o600)
        
        # If exclusive creation is enabled, check if the file exists
        if exclusive and os.fstat(fd).st_size > 0:
            raise FileExistsError(f"File {file_path} already exists and cannot be created exclusively.")
        
        # Perform operations on the file
        # For example, write to the file:
        os.write(fd, b"Some data to write to the file")
        
        # Close the file descriptor
        os.close(fd)
        
        return True
    except FileExistsError:
        # Handle the case where the file already exists and exclusive creation is enabled
        print(f"Error: File {file_path} already exists and cannot be created exclusively.")
        return False
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    file_path = "example.txt"
    
    # Create a new file or open an existing file, truncating it to 0 bytes
    if create_or_open_file(file_path, truncate=True):
        print(f"File {file_path} created or opened successfully and truncated to 0 bytes.")
    
    # Create a new file or open an existing file, but fail if the file already exists
    if create_or_open_file(file_path, exclusive=True):
        print(f"File {file_path} created or opened successfully.")
    else:
        print(f"File {file_path} already exists and cannot be created exclusively.")
    
    # Example of writing to the file
    with open(file_path, 'a') as file:
        file.write("Some more data to write to the file.")
    
    # Example of reading from the file
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)