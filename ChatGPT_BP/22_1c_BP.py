import os

def read_file_from_safe_directory(file_name, safe_directory):
    try:
        # Ensure the file name is safe and does not include any directory traversal characters
        if not os.path.basename(file_name) == file_name:
            raise ValueError("Invalid file name.")
        
        # Construct the full path and ensure it's within the safe directory
        file_path = os.path.join(safe_directory, file_name)
        safe_directory = os.path.abspath(safe_directory)
        file_path = os.path.abspath(file_path)
        
        if not file_path.startswith(safe_directory):
            raise ValueError("Attempted directory traversal detected.")
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist in the directory '{safe_directory}'.")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, not a file.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_name}'.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
safe_directory = "/path/to/safe/directory"
file_name = "example.txt"
file_content = read_file_from_safe_directory(file_name, safe_directory)
if file_content:
    print(file_content)