import os

def read_file_from_safe_directory(filename):
    safe_directory = '/safe/'
    file_path = os.path.join(safe_directory, filename)
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: An error occurred while reading the file."

# Example usage
filename = 'example.txt'
file_content = read_file_from_safe_directory(filename)
print(file_content)