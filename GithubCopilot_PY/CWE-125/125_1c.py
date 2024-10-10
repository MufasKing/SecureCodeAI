import sys

def getValueFromArray(array, size, index):
    if 0 <= index < size:
        return array[index]
    else:
        return -1

def main():
    try:
        index = int(input("Enter an index: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(-1)
    
    id_sequence = [10, 20, 30, 40, 50]  # Example array
    size = len(id_sequence)
    
    result = getValueFromArray(id_sequence, size, index)
    sys.exit(result)

if __name__ == "__main__":
    main()