import mysql.connector
from mysql.connector import Error
import os
from PIL import Image

def connect_to_database(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def insert_image(connection, file_path):
    cursor = connection.cursor()
    try:
        # Validate file path
        if not os.path.isfile(file_path):
            raise ValueError("File does not exist")
        
        # Secure file access
        with open(file_path, "rb") as file:
            binary_data = file.read()
            # Ensure the file is an image
            try:
                Image.open(file_path)
            except IOError:
                raise ValueError("The file is not a valid image")
            
            # Parameterized query
            query = "INSERT INTO images (image_data) VALUES (%s)"
            cursor.execute(query, (binary_data,))
            connection.commit()
            print("Image inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

# Example usage
if __name__ == "__main__":
    db_connection = connect_to_database("your_host", "your_username", "your_password", "your_db_name")
    if db_connection:
        insert_image(db_connection, "/path/to/your/image.jpg")
        db_connection.close()