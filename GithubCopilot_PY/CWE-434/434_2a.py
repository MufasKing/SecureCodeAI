import mysql.connector
from mysql.connector import Error
from PIL import Image
import io

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    """Create a table to store images if it doesn't exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        image LONGBLOB NOT NULL
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()

def convert_to_binary_data(filename):
    """Convert digital data to binary format."""
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_image(connection, image_data):
    """Insert image into the database."""
    cursor = connection.cursor()
    sql_insert_blob_query = """ INSERT INTO images (image) VALUES (%s)"""
    cursor.execute(sql_insert_blob_query, (image_data,))
    connection.commit()
    print("Image inserted successfully as a BLOB into images table")

def main():
    image_path = input("Enter the path to the image file: ")
    connection = create_connection()
    if connection is not None:
        create_table(connection)
        image_data = convert_to_binary_data(image_path)
        insert_image(connection, image_data)
        connection.close()

if __name__ == "__main__":
    main()