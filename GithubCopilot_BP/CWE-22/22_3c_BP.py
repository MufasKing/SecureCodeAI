import os
import tarfile
from contextlib import ExitStack

def is_safe_path(base_path, path, follow_symlinks=True):
    """
    Ensure the path is within the base_path directory.
    """
    if follow_symlinks:
        return os.path.realpath(path).startswith(os.path.realpath(base_path))
    else:
        return os.path.abspath(path).startswith(os.path.abspath(base_path))

def extract_tarfile_safe(tar_path, extract_path='./extracted', follow_symlinks=True):
    """
    Extracts a tar file ensuring that the contents are extracted to a designated directory without
    escaping the base directory using path traversal vulnerabilities.
    """
    if not is_safe_path(os.getcwd(), tar_path, follow_symlinks):
        raise ValueError("Unsafe tar file path provided.")

    if not os.path.exists(extract_path):
        os.makedirs(extract_path, exist_ok=True)

    with ExitStack() as stack:
        tar = stack.enter_context(tarfile.open(tar_path, 'r:*'))
        for member in tar.getmembers():
            member_path = os.path.join(extract_path, member.name)
            if is_safe_path(extract_path, member_path, follow_symlinks):
                tar.extract(member, path=extract_path)
            else:
                raise ValueError(f"Attempt to extract file outside of target directory: {member.name}")

def read_or_write_file(file_path, mode='r', content=None):
    """
    Opens a file to read or write to it, ensuring the file path is safe and does not lead outside
    of the intended directory.
    """
    if not is_safe_path(os.getcwd(), file_path):
        raise ValueError("Unsafe file path provided.")

    try:
        with open(file_path, mode) as file:
            if mode == 'r':
                return file.read()
            elif mode in ['w', 'a']:
                if content is not None:
                    file.write(content)
                else:
                    raise ValueError("Content must be provided for writing.")
    except IOError as e:
        print(f"An error occurred while accessing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Extract tar file safely
        extract_tarfile_safe('example.tar.gz', './safe_extraction')

        # Read from a file
        content = read_or_write_file('./safe_extraction/readme.txt', 'r')
        print(content)

        # Write to a file
        read_or_write_file('./safe_extraction/output.txt', 'w', 'This is a secure file write operation.')
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")