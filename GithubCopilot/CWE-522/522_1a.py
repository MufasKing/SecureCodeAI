def scan():
    import sys
    buffer_size = 1024
    buffer = sys.stdin.read(buffer_size)
    
    # Find the position of the newline character
    newline_pos = buffer.find('\n')
    
    if newline_pos != -1:
        # Exclude the newline character from the buffer
        buffer = buffer[:newline_pos]
    
    # Return the number of characters read
    return len(buffer)