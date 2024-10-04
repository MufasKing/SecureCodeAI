import os

def secure_file_creation(file_path):
    # Define the file flags
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
    
    # Define the file mode (permissions)
    mode = 0o600  # 600 is the octal representation of read/write for the owner only
    
    try:
        # Use the os.open() function with the defined flags and mode
        file_descriptor = os.open(file_path, flags, mode)
        
        # Open the file descriptor for writing
        with os.fdopen(file_descriptor, 'w') as file:
            # Write to the file
            file.write('Secure file creation and handling example.')
            
            # Flush and close the file
            file.flush()
            file.close()
            
        # Close the file descriptor
        os.close(file_descriptor)
        
        print(f"File '{file_path}' created successfully.")
    except OSError as e:
        # Handle specific errors
        if e.errno == os.errno.EEXIST:
            print("Error: File already exists.")
        elif e.errno == os.errno.ENOENT:
            print("Error: No such directory.")
        else:
            print(f"An error occurred: {e.strerror}")
    finally:
        # Ensure the file is closed even if an exception occurs
        if 'file_descriptor' in locals():
            os.close(file_descriptor)

# Example usage
secure_file_creation("secure_file.txt")