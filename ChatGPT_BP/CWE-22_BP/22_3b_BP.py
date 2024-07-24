import os
import tarfile
import zipfile
import tempfile
import shutil

def extract_archive(archive_path, extract_to):
    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    try:
        # Open the archive file
        if tarfile.is_tarfile(archive_path):
            with tarfile.open(archive_path, 'r:*') as archive:
                archive.extractall(path=extract_to)
        elif zipfile.is_zipfile(archive_path):
            with zipfile.ZipFile(archive_path, 'r') as archive:
                archive.extractall(path=extract_to)
        else:
            raise ValueError("Unsupported archive format")
        
        print(f"Successfully extracted to {extract_to}")

        # Validate extracted files
        for root, dirs, files in os.walk(extract_to):
            for name in files:
                file_path = os.path.join(root, name)
                if not os.path.isfile(file_path):
                    raise ValueError(f"File validation failed: {file_path} is not a valid file")
        
        print("All files validated successfully.")

    except (tarfile.TarError, zipfile.BadZipFile, ValueError) as e:
        print(f"An error occurred: {e}")
        # Cleanup the extraction directory if extraction fails
        if os.path.exists(extract_to):
            shutil.rmtree(extract_to)
        print("Cleaned up extraction directory due to error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        if os.path.exists(extract_to):
            shutil.rmtree(extract_to)
        print("Cleaned up extraction directory due to unexpected error.")
    else:
        # Cleanup: Optionally remove the extracted files if no errors occurred
        pass

if __name__ == "__main__":
    archive_path = 'archive.zip'
    extract_to = '/tmp/unpack'

    # Use a temporary directory for extraction
    with tempfile.TemporaryDirectory() as tmp_extract_to:
        extract_archive(archive_path, tmp_extract_to)
        
        # Move the successfully extracted files to the final directory
        if os.path.exists(tmp_extract_to) and os.path.isdir(tmp_extract_to):
            if os.path.exists(extract_to):
                shutil.rmtree(extract_to)
            shutil.move(tmp_extract_to, extract_to)
            print(f"Files moved to {extract_to}")
        else:
            print("No files to move, cleanup complete.")