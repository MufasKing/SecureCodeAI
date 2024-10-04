import os

def create_or_open_file(filename, mode='w'):
    """Create a new file or open an existing file."""
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL
    return os.open(filename, flags, 0o666)

if __name__ == '__main__':
    with create_or_open_file('test.txt') as f:
        f.write('Hello, world!')