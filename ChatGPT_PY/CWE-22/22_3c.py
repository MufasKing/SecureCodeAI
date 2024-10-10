import tarfile
import os

# Define file names and paths
tar_filename = 'example_archive.tar.gz'
file_to_archive = 'example_file.txt'
extracted_dir = 'extracted_files/'

# Create a sample file to archive
with open(file_to_archive, 'w') as file:
    file.write('This is a sample file to be archived.')

# Create a tar.gz archive
with tarfile.open(tar_filename, 'w:gz') as tar:
    tar.add(file_to_archive, arcname=os.path.basename(file_to_archive))

# Extract the tar.gz archive
with tarfile.open(tar_filename, 'r:gz') as tar:
    # Create the directory for extraction if it doesn't exist
    os.makedirs(extracted_dir, exist_ok=True)
    tar.extractall(path=extracted_dir)

print(f"Archive '{tar_filename}' created and extracted successfully.")
