import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python 416_1b.py <buffer_size>")
        sys.exit(1)

    try:
        buffer_size = int(sys.argv[1])
    except ValueError:
        print("Buffer size must be an integer.")
        sys.exit(1)

    buffer = bytearray(buffer_size)
    print(buffer)

if __name__ == "__main__":
    main()