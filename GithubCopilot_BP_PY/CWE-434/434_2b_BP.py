import base64
import os
import sqlite3
from sqlite3 import Error
import hashlib
import logging
import binascii

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        logging.error(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table if it doesn't already exist"""
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS images
                     (id INTEGER PRIMARY KEY, name TEXT, image_data TEXT)''')
    except Error as e:
        logging.error(f"Error creating table: {e}")

def secure_salt_generation():
    """Generate a secure salt"""
    return os.urandom(16)

def secure_hashing(data, salt):
    """Generate a secure hash for the given data using the provided salt"""
    return hashlib.pbkdf2_hmac('sha256', data.encode(), salt, 100000)

def insert_image(conn, name, image_data):
    """Insert an image into the database securely"""
    try:
        c = conn.cursor()
        # Securely generate salt and hash the image data
        salt = secure_salt_generation()
        hashed_image_data = secure_hashing(image_data, salt)
        # Convert the hashed image data to a storable format
        storable_image_data = binascii.hexlify(hashed_image_data).decode()
        # Use a prepared statement to securely insert data
        c.execute("INSERT INTO images (name, image_data) VALUES (?, ?)", (name, storable_image_data))
        conn.commit()
    except Error as e:
        logging.error(f"Error inserting image into database: {e}")

def read_and_convert_image_to_base64(image_path):
    """Read an image and convert it to base64"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except IOError as e:
        logging.error(f"Error reading image file: {e}")
        return None

def upload_image(image_path, db_path):
    """Main function to handle the upload and storage of an image"""
    # Read and convert the image to base64
    image_data = read_and_convert_image_to_base64(image_path)
    if image_data is None:
        return
    # Extract image name
    image_name = os.path.basename(image_path)
    # Connect to the database
    conn = create_connection(db_path)
    if conn is not None:
        create_table(conn)
        insert_image(conn, image_name, image_data)
        logging.info(f"Image '{image_name}' uploaded successfully.")
        conn.close()
    else:
        logging.error("Failed to connect to the database.")

# Example usage
if __name__ == "__main__":
    upload_image("path/to/your/image.jpg", "path/to/your/database.db")