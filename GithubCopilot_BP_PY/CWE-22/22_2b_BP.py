from flask import Flask, send_from_directory, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the base directory for images
IMAGES_DIR = os.path.join(app.root_path, 'images')

@app.route('/images/<filename>')
def serve_image(filename):
    try:
        # Secure the filename to prevent directory traversal
        secure_name = secure_filename(filename)
        # Check if the file exists to prevent unauthorized access
        if not os.path.exists(os.path.join(IMAGES_DIR, secure_name)):
            # If the file does not exist, return a 404 error
            abort(404)
        # Serve the file from the images directory
        return send_from_directory(IMAGES_DIR, secure_name)
    except Exception as e:
        # Log the error or handle it as needed
        print(f"An error occurred: {e}")
        # Return a generic error message to the user
        abort(500)

if __name__ == '__main__':
    app.run( )