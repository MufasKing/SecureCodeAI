import os

def write_important_config():
    # Define the path for the file
    file_path = "important_config"
    
    # Define the flags for opening the file
    # O_WRONLY - Open for writing only
    # O_CREAT - Create file if it does not exist
    flags = os.O_WRONLY | os.O_CREAT
    
    # Define the mode for the new file
    # S_IRUSR - User read permission
    # S_IWUSR - User write permission
    mode = os.S_IRUSR | os.S_IWUSR
    
    try:
        # Open the file with the specified flags and mode
        file_descriptor = os.open(file_path, flags, mode)
        
        # Write the string "important_config" to the file
        os.write(file_descriptor, b"important_config")
        
    except OSError as e:
        # Handle errors during file access
        print(f"Error opening/writing to file: {e}")
    finally:
        # Ensure the file is closed properly
        if 'file_descriptor' in locals():
            os.close(file_descriptor)
            print("File closed successfully.")
        else:
            print("File was not opened, no need to close.")

# Call the function to perform the operation
write_important_config()