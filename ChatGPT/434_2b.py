import sqlite3
import base64

def upload_image(image_path):
    # Read and encode image to base64
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Extract the image name from the path
    image_name = image_path.split('/')[-1]
    
    # Insert the image name and base64 string into the database
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO images (name, image_base64)
        VALUES (?, ?)
    ''', (image_name, image_base64))
    
    conn.commit()
    conn.close()
    print(f"Image {image_name} has been uploaded and stored in the database.")

# Example usage
upload_image('path/to/your/image.jpg')
