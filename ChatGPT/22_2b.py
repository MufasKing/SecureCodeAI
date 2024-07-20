from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
IMAGE_FOLDER = 'images'  # Path to the folder containing images

@app.route('/images/<filename>')
def serve_image(filename):
    file_path = os.path.join(IMAGE_FOLDER, filename)
    
    if os.path.isfile(file_path):
        return send_from_directory(IMAGE_FOLDER, filename)
    else:
        abort(404)  # Return a 404 error if the file does not exist

if __name__ == '__main__':
    app.run(debug=True)
