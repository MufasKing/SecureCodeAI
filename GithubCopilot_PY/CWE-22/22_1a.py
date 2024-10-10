import os

# Define the file path
file_path = os.path.join('/safe/', 'your_file.txt')

# Open and read the file
try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")