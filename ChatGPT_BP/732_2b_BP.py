import os
import errno

def open_file_securely(file_path):
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_EXCL
    mode = 0o600  # File permission: owner read/write

    try:
        # Check if the file already exists
        if os.path.exists(file_path):
            raise FileExistsError(f"File '{file_path}' already exists.")

        # Open the file with specified flags and mode
        fd = os.open(file_path, flags, mode)
        
        try:
            # Open a file object using the file descriptor
            with os.fdopen(fd, 'w') as file:
                # Write data to the file
                file.write("Secure file handling example.")
                print(f"File '{file_path}' created and written successfully.")
        
        except Exception as e:
            # If an exception occurs while writing, close the file descriptor
            os.close(fd)
            raise e

    except FileExistsError as fe:
        print(fe)
    except OSError as oe:
        if oe.errno == errno.EEXIST:
            print(f"Failed to create '{file_path}': File already exists.")
        else:
            print(f"Failed to create '{file_path}': {oe.strerror}")

# Example usage
open_file_securely('/path/to/your/file.txt')