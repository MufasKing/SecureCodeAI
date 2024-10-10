import os

def read_file_from_safe_directory(safe_directory, filename):
    # Ensure the safe directory is an absolute path
    safe_directory = os.path.abspath(safe_directory)
    
    # Construct the full file path
    file_path = os.path.join(safe_directory, filename)
    
    # Check if the file path is within the safe directory
    if not file_path.startswith(safe_directory):
        raise ValueError("Attempt to access a file outside the safe directory")
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
safe_directory = "/path/to/safe/directory"
filename = "example.txt"
print(read_file_from_safe_directory(safe_directory, filename))