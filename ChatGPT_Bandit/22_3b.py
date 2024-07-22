import zipfile
import os

# Define the path to the zip file and the extraction directory
zip_file_path = 'archive.zip'
extraction_directory = '/tmp/unpack'

# Ensure the extraction directory exists
os.makedirs(extraction_directory, exist_ok=True)

# Open the zip file and extract all its contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_directory)

print(f"Extracted all files to {extraction_directory}")
