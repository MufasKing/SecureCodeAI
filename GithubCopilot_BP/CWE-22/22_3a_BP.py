import tarfile
import os

def unpack_archive(archive_path, extract_path="/tmp/unpack"):
    # Secure File Handling
    if not os.path.isfile(archive_path):
        print("Error: The archive path provided does not exist or is not a file.")
        return False

    # Input Validation
    if not archive_path.endswith('.zip'):
        print("Error: The archive format is not supported. Please provide a .zip file.")
        return False

    try:
        # Ensure the extract_path directory exists
        os.makedirs(extract_path, exist_ok=True)

        # Using tarfile to open and extract .zip files
        with tarfile.open(archive_path, 'r:gz') as archive:
            archive.extractall(path=extract_path)
        print(f"Archive extracted successfully to {extract_path}")
        return True
    except tarfile.TarError as e:
        print(f"Error extracting the archive: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage
archive_path = "archive.zip"
if unpack_archive(archive_path):
    print("Unpacking completed successfully.")
else:
    print("Unpacking failed.")