import os

def read_safe_file(filename):
    base_dir = os.path.abspath('/safe/')  # Define the base directory securely
    try:
        # Ensure the requested file path is secure
        requested_path = os.path.join(base_dir, filename)
        requested_path = os.path.abspath(requested_path)

        # Validate that the requested file is within the /safe/ directory
        if not requested_path.startswith(base_dir):
            raise ValueError("Invalid file path: Potential directory traversal attempt detected")

        # Securely open and read the file
        with open(requested_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return content

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("Error: An unexpected error occurred.")
    return None

# Example usage
filename = "example.txt"
content = read_safe_file(filename)
if content:
    print(content)