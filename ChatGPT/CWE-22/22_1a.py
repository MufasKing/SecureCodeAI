import os

def read_file_from_safe_directory(filename):
    # Define the path to the /safe/ directory
    directory = '/safe/'
    
    # Construct the full file path
    file_path = os.path.join(directory, filename)
    
    # Check if the file exists before attempting to read
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except Exception as e:
            return f"An error occurred while reading the file: {e}"
    else:
        return "File does not exist."

# Example usage
filename = 'yourfile.txt'  # Replace with your actual file name
file_content = read_file_from_safe_directory(filename)
print(file_content)
