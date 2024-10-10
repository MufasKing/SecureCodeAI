import os
import tarfile
import shutil

def is_within_directory(directory, target):
    """Ensure the target path is within the directory."""
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)
    return os.path.commonpath([abs_directory]) == os.path.commonpath([abs_directory, abs_target])

def extract_tarfile(tar_path, extract_to):
    """Extract tarfile contents to a specified directory."""
    if not os.path.isfile(tar_path):
        raise ValueError("The specified tarfile does not exist or is not a file.")
    if not tarfile.is_tarfile(tar_path):
        raise ValueError("The specified file is not a valid tarfile.")

    os.makedirs(extract_to, exist_ok=True)
    
    try:
        with tarfile.open(tar_path, 'r:*') as tar:
            for member in tar.getmembers():
                member_path = os.path.join(extract_to, member.name)
                if not is_within_directory(extract_to, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
            tar.extractall(path=extract_to)
        print(f"Extracted tarfile to {extract_to} successfully.")
    except (tarfile.TarError, IOError, Exception) as e:
        print(f"An error occurred: {e}")
        shutil.rmtree(extract_to)  # Clean up extracted files if there's an error
        raise

if __name__ == "__main__":
    tar_path = "archive.zip"  # Replace with your actual tar file path
    extract_to = "/tmp/unpack"
    
    try:
        extract_tarfile(tar_path, extract_to)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")