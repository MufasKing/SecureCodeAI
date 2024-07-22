import base64
import sqlite3
import hashlib
import os
import logging
from werkzeug.utils import secure_filename
from contextlib import closing

# Configure logging
logging.basicConfig(filename='image_upload.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Database configuration
DATABASE = 'secure_image_upload.db'

# Secure table creation
def create_table():
    try:
        with sqlite3.connect(DATABASE) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS images (
                    id INTEGER PRIMARY KEY,
                    image_name TEXT NOT NULL,
                    image_data BLOB NOT NULL,
                    salt TEXT NOT NULL
                )
                """)
                conn.commit()
                logging.info('Table created successfully.')
    except sqlite3.Error as e:
        logging.error(f'Error creating table: {e}')

# Function to generate a secure salt
def generate_salt():
    return os.urandom(16)

# Function to securely hash image data
def hash_image_data(image_data, salt):
    hasher = hashlib.sha256()
    hasher.update(salt + image_data)
    return hasher.digest()

# Function to handle image upload
def upload_image(image_path):
    try:
        # Secure file handling: ensure a valid and secure filename
        filename = secure_filename(os.path.basename(image_path))
        
        # Read and encode image to base64
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            image_b64 = base64.b64encode(image_data).decode('utf-8')
        
        # Generate salt and hash the image data
        salt = generate_salt()
        hashed_data = hash_image_data(image_data, salt)

        # Insert into the database using prepared statements
        with sqlite3.connect(DATABASE) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("""
                INSERT INTO images (image_name, image_data, salt) 
                VALUES (?, ?, ?)
                """, (filename, hashed_data, salt))
                conn.commit()
                logging.info(f'Image {filename} uploaded and stored successfully.')
    except (sqlite3.Error, IOError) as e:
        logging.error(f'Error during image upload: {e}')
        print(f'An error occurred: {e}')

# Run table creation on script execution
if __name__ == "__main__":
    create_table()