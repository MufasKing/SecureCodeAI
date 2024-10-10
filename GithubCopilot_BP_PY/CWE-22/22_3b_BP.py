import tarfile
import tempfile
import os
import shutil

def extract_tarfile_to_temp_directory(archive_path):
    # Step 1: Validate the archive file
    if not os.path.isfile(archive_path):
        raise FileNotFoundError(f"The archive file {archive_path} does not exist.")
    if not tarfile.is_tarfile(archive_path):
        raise ValueError(f"The file {archive_path} is not a valid tar archive.")

    # Step 2: Use a temporary directory for extraction
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Step 3: Open the tarfile and extract it to the temporary directory
            with tarfile.open(archive_path, "r") as tar:
                tar.extractall(path=temp_dir)
                print(f"Successfully extracted {archive_path} to {temp_dir}")

            # Step 4: Move extracted files to the target directory (/tmp/unpack)
            target_dir = "/tmp/unpack"
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            for file_name in os.listdir(temp_dir):
                shutil.move(os.path.join(temp_dir, file_name), target_dir)
            print(f"All files have been moved to {target_dir}")

        except Exception as e:
            # Handle errors during extraction and moving
            print(f"An error occurred: {e}")

        finally:
            # Step 5: Cleanup is handled by the TemporaryDirectory context manager automatically

if __name__ == "__main__":
    archive_path = "archive.zip"
    extract_tarfile_to_temp_directory(archive_path)