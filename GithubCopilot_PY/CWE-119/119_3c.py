import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python argv_index.py <index>")
        return

    try:
        index = int(sys.argv[1])
        print(sys.argv[index + 1])
    except ValueError:
        print("Please provide a valid integer index.")
    except IndexError:
        print("Index out of range. Please provide a valid index.")

if __name__ == "__main__":
    main()