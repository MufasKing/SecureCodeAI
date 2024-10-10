import tarfile

# Define the file paths
tar_file_path = 'example.tar.gz'
extract_path = 'extracted_files'

# Use the with statement to open the tar file
with tarfile.open(tar_file_path, 'r:gz') as tar:
    # Extract all the contents of the tar file
    tar.extractall(path=extract_path)

# Use the with statement to open a file for writing
with open('example.txt', 'w') as file:
    file.write('This is an example text file.')