MAX_BUFFER_SIZE = 256

message = "Hello"
if len(message) >= MAX_BUFFER_SIZE:
  raise ValueError("Message is too long")

buffer = bytearray(MAX_BUFFER_SIZE)

# copy the message to the buffer
buffer[:len(message)] = message.encode()