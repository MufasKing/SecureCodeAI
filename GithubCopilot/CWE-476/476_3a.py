import sys

def allocate_and_copy():
    # Allocate the first buffer
    buf = bytearray(1024)
    print("Enter up to 100 characters for the first buffer:")
    input_data = sys.stdin.read(100)
    buf[:len(input_data)] = input_data.encode('utf-8')

    # Allocate the second buffer
    buf1 = bytearray(1024)
    print("Enter up to 100 characters for the second buffer:")
    input_data1 = sys.stdin.read(100)
    buf1[:len(input_data1)] = input_data1.encode('utf-8')

    return buf, buf1

# Example usage
if __name__ == "__main__":
    buf, buf1 = allocate_and_copy()
    print("First buffer content:", buf[:100].decode('utf-8'))
    print("Second buffer content:", buf1[:100].decode('utf-8'))