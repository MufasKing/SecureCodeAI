import os
import tarfile
import tempfile

def is_within_directory(directory, target):
    """Check if the target path is within the specified directory."""
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)
    return os.path.commonprefix([abs_directory, abs_target]) == abs_directory

def safe_extract(tar, path="."):
    """Extract files from a tar archive safely to avoid path traversal issues."""
    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise Exception("Attempted Path Traversal in Tar File")
    tar.extractall(path)

def extract_tar_file(tar_path, extract_to):
    """Extract a tar file to a specified directory safely."""
    # Input validation
    if not os.path.isfile(tar_path):
        raise FileNotFoundError(f"The file {tar_path} does not exist.")
    if not tarfile.is_tarfile(tar_path):
        raise tarfile.ReadError(f"The file {tar_path} is not a valid tar archive.")

    try:
        with tarfile.open(tar_path, "r:*") as tar:
            safe_extract(tar, path=extract_to)
            print(f"Extracted {tar_path} to {extract_to}")
    except (tarfile.TarError, Exception) as e:
        print(f"Error extracting tar file {tar_path}: {e}")

def write_to_file(file_path, data):
    """Write data to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            print(f"Data written to {file_path}")
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def main():
    # Example usage
    tar_path = "example.tar.gz"
    extract_to = tempfile.mkdtemp()
    output_file = os.path.join(extract_to, "output.txt")
    
    try:
        extract_tar_file(tar_path, extract_to)
        write_to_file(output_file, "This is an example text.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()