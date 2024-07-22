import os
import mysql.connector
from mysql.connector import Error
from PIL import Image

def validate_image(file_path):
    """Validate if the file is a proper image."""
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception as e:
        print(f"Image validation error: {e}")
        return False

def connect_to_database():
    """Create a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='image_db',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None

def store_image(file_path):
    """Store the image file in the MySQL database."""
    if not validate_image(file_path):
        print("Invalid image file.")
        return
    
    connection = connect_to_database()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        with open(file_path, 'rb') as file:
            image_data = file.read()
        
        cursor = connection.cursor()
        query = "INSERT INTO images (image_name, image_data) VALUES (%s, %s)"
        cursor.execute(query, (os.path.basename(file_path), image_data))
        connection.commit()
        print(f"Image {os.path.basename(file_path)} stored successfully.")
    
    except Error as e:
        print(f"Error while storing the image: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    file_path = input("Enter the path to the image file: ").strip()
    if not os.path.isfile(file_path):
        print("The file does not exist.")
        return
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        print("Unsupported file format.")
        return

    store_image(file_path)

if __name__ == "__main__":
    main()