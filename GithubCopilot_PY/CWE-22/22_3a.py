import tarfile
import os

# Define the path to the archive file and the destination directory
archive_path = 'archive.zip'
destination_dir = '/tmp/unpack'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Open the archive file and extract all files to the destination directory
with tarfile.open(archive_path, 'r:gz') as archive:
    archive.extractall(path=destination_dir)