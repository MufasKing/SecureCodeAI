import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python 119_2b.py <index>")
        return

    try:
        index = int(sys.argv[1])
    except ValueError:
        print("Invalid input: not an integer")
        return

    array = [10, 20, 30, 40, 50]  # Example array

    if 0 <= index < len(array):
        print(array[index])
    else:
        print("Invalid input: index out of range")

if __name__ == "__main__":
    main()