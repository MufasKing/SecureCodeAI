import os

def safe_file_read(file_path, safe_dir):
    """
    Reads the content of a file within a safe directory securely.
    Prevents directory traversal and ensures the file is within the specified safe directory.

    Parameters:
    - file_path: The path to the file to be read.
    - safe_dir: The directory considered safe to read files from.

    Returns:
    - The content of the file if it's within the safe directory and exists.
    - None, if the file is outside the safe directory or an error occurs.
    """

    # Normalize the paths to prevent directory traversal
    safe_dir = os.path.normpath(safe_dir)
    full_path = os.path.normpath(os.path.join(safe_dir, file_path))

    # Check if the file is within the safe directory
    if not full_path.startswith(safe_dir):
        print("Access denied: Attempt to access a file outside the safe directory.")
        return None

    # Attempt to read the file
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

# Example usage
safe_dir = "/path/to/safe/directory"
file_path = input("Enter the relative path of the file to read: ").strip()
content = safe_file_read(file_path, safe_dir)
if content is not None:
    print("File content:")
    print(content)
else:
    print("Failed to read the file.")