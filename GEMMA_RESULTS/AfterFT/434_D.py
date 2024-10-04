from os import environ, remove
from base64 import b64encode
from cryptography.fernet import Fernet

# Generate a random key for encryption
key = Fernet.generate_key()

# Store the encryption key securely in an environment variable
environ.setdefault('ENCRYPTION_KEY', key.decode())

def upload_image():
    try:
        # Get the uploaded file
        file = request.files['image']

        # Check if the file is an image
        if file and file.content_type.startswith('image'):
            # Read the file
            file_data = file.read()

            # Encode the image data
            encoded_data = b64encode(file_data)

            # Encrypt the encoded data
            fernet = Fernet(key.decode())
            encrypted_data = fernet.encrypt(encoded_data)

            # Write the encrypted data to a file
            with open('encoded_image.enc', 'wb') as file:
                file.write(encrypted_data)

            print("Image uploaded and encrypted successfully.")

        else:
            print("Invalid file type. Please upload an image.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Remove the temporary file if it exists
        try:
            remove('encoded_image.enc')
        except Exception as e:
            print(f"Error removing file: {e}")

# Call the upload_image function
upload_image()