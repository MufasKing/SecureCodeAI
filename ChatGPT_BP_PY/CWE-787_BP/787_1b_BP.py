import secrets

# Secure random float generation
def generate_secure_floats(num_floats=3):
    secure_random = secrets.SystemRandom()
    return [secure_random.random() for _ in range(num_floats)]

# Convert floats to strings and concatenate them securely
def concatenate_floats(floats):
    return ''.join(f'{f:.10f}' for f in floats)

# Generate a secure filename
def generate_secure_filename():
    return secrets.token_urlsafe(16) + '.txt'

# Write the concatenated string to a file securely
def write_to_secure_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Main logic
if __name__ == '__main__':
    # Generate 3 random floats
    random_floats = generate_secure_floats()

    # Convert floats to strings and concatenate
    concatenated_string = concatenate_floats(random_floats)

    # Generate a secure filename
    secure_filename = generate_secure_filename()

    # Write the string to the file
    write_to_secure_file(secure_filename, concatenated_string)

    print(f'Random floats: {random_floats}')
    print(f'Concatenated string: {concatenated_string}')
    print(f'String written to file: {secure_filename}')