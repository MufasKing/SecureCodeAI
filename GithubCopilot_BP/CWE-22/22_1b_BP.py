import os

def read_file_securely(filename):
    # Define the safe base directory
    safe_base_path = "/safe/"
    
    # Validate the filename to avoid directory traversal attacks
    if not os.path.basename(filename) == filename:
        raise ValueError("Invalid filename. Directory traversal is not allowed.")
    
    # Construct the full path and ensure it's within the safe directory
    full_path = os.path.abspath(os.path.join(safe_base_path, filename))
    if not full_path.startswith(os.path.abspath(safe_base_path)):
        raise ValueError("Access denied. File is outside the allowed directory.")
    
    try:
        # Open the file in read-only mode to avoid unintended modifications
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        # Handle file not found error without revealing the path or existence
        raise FileNotFoundError("Requested file is not available.")
    except Exception as e:
        # Generic exception handling to avoid information leaks
        raise Exception("An error occurred while reading the file.") from e