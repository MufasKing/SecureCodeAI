import mysql.connector
from mysql.connector import Error
from PIL import Image
import io

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='your_host',           # Replace with your MySQL server host
            user='your_username',       # Replace with your MySQL username
            password='your_password',   # Replace with your MySQL password
            database='your_database'    # Replace with your MySQL database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to create the table if it doesn't exist
def create_table_if_not_exists(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INT AUTO_INCREMENT PRIMARY KEY,
                image LONGBLOB NOT NULL
            )
        """)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to insert an image into the database
def insert_image(connection, image_path):
    try:
        cursor = connection.cursor()
        with open(image_path, 'rb') as file:
            binary_data = file.read()
            cursor.execute("INSERT INTO images (image) VALUES (%s)", (binary_data,))
            connection.commit()
            print("Image inserted successfully")
    except Error as e:
        print(f"Error: {e}")

# Main function
def main():
    image_path = input("Enter the path of the image file to upload: ")
    connection = connect_to_database()
    if connection:
        create_table_if_not_exists(connection)
        insert_image(connection, image_path)
        connection.close()

if __name__ == "__main__":
    main()
