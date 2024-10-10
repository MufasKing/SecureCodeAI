import os
import secrets
import json

def generate_secure_data_and_write_to_file():
    # Generate 3 random floats securely
    random_floats = [secrets.SystemRandom().uniform(0, 1) for _ in range(3)]
    
    # Convert them to strings securely
    string_floats = [f"{float_val:.17f}" for float_val in random_floats]
    
    # Concatenate them into a single string
    concatenated_string = ''.join(string_floats)
    
    # Generate a secure filename
    secure_filename = "secure_data_" + secrets.token_hex(8) + ".txt"
    
    # Secure file operations
    with open(secure_filename, 'w', encoding='utf-8') as file:
        # Write the concatenated string to the file
        file.write(concatenated_string)
    
    print(f"Data written to {secure_filename}")

generate_secure_data_and_write_to_file()