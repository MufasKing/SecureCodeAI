def get_value_at_index(id_sequence, index):
    try:
        value = id_sequence[index]
        return value
    except IndexError:
        return -1

def main():
    id_sequence = [10, 20, 30, 40, 50]  # Example array id_sequence
    try:
        index = int(input("Enter an index to retrieve from id_sequence: "))
        
        if index < 0 or index >= len(id_sequence):
            print("Index is out of bounds.")
        else:
            result = get_value_at_index(id_sequence, index)
            if result == -1:
                print("Index is out of bounds.")
            else:
                print(f"The value at index {index} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter an integer index.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()