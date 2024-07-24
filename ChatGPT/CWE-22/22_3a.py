import zipfile
import os

def unzip_archive(zip_path, extract_to):
    # Ensure the destination directory exists
    os.makedirs(extract_to, exist_ok=True)

    # Open the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents into the specified directory
        zip_ref.extractall(extract_to)

# Define the path to the ZIP file and the extraction directory
zip_path = 'archive.zip'
extract_to = '/tmp/unpack'

# Call the function to unzip the archive
unzip_archive(zip_path, extract_to)

print(f"All files have been extracted to {extract_to}")
