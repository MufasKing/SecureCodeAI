def get_value(array, index):
    if index < 0:
        return -1
    elif index > len(array):
        return -1
    else:
        return array[index]

def main():
    array = [1, 2, 3, 4, 5]
    index = int(input("Enter the index: "))
    print(get_value(array, index))

if __name__ == "__main__":
    main()