import tarfile
import os

# Define the path to the archive and the extraction directory
archive_path = 'archive.zip'
extract_dir = '/tmp/unpack'

# Create the extraction directory if it doesn't exist
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# Open the archive file and extract all files
with tarfile.open(archive_path, 'r:gz') as archive:
    archive.extractall(path=extract_dir)

print(f"All files extracted to {extract_dir}")