import base64
import sqlite3

def upload_image(image_path, image_name):
    # Read the image file in binary mode
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # Convert the image to a base64 string
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    # Insert the image name and base64 string into the database
    cursor.execute('''
        INSERT INTO images (name, data)
        VALUES (?, ?)
    ''', (image_name, image_base64))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Example usage
upload_image('path/to/your/image.jpg', 'example_image')