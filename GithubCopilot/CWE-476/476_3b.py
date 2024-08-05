def scan():
    import sys
    input_buffer = sys.stdin.read(1024)  # Read up to 1024 bytes from standard input
    newline_index = input_buffer.find('\n')  # Find the index of the newline character

    if newline_index != -1:
        input_string = input_buffer[:newline_index]  # Extract the string up to the newline character
        return len(input_string)  # Return the number of characters read in
    else:
        return len(input_buffer)  # If no newline character, return the length of the entire buffer

# Example usage:
# To test this function, you would need to provide input via standard input.
# For example, you can run this script and type input followed by Enter.
if __name__ == "__main__":
    print("Number of characters read:", scan())