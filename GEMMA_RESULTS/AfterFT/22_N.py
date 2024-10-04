import os
from pathlib import Path

def secure_file_read(file_path):
    # Define the safe directory
    safe_directory = "/safe/"
    
    # Validate the file path
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    
    # Remove any unsafe characters from the file path
    sanitized_file_path = os.path.normpath(file_path).replace("\\", "/").replace("..", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
    
    # Construct the full file path
    full_file_path = os.path.join(safe_directory, sanitized_file_path)
    
    # Check if the file exists and is a file
    if not os.path.isfile(full_file_path):
        raise FileNotFoundError("File not found.")
    
    # Check if the file is in the /safe/ directory
    if not full_file_path.startswith(safe_directory):
        raise PermissionError("Access denied.")
    
    try:
        # Open the file in read mode
        with open(full_file_path, "r") as file:
            # Read the file contents
            contents = file.read()
            return contents
    except Exception as e:
        # Handle any exceptions that occur during file reading
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = input("Enter the file path: ")

# Call the function to read the file
file_contents = secure_file_read(file_path)

if file_contents:
    print("File contents:")
    print(file_contents)
else:
    print("Failed to read the file.")