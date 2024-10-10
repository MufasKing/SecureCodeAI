from flask import Flask, send_file, abort
import os

app = Flask(__name__)

def validate_image(f):
    def wrapper(name):
        # Input sanitization to ensure the filename is secure
        name = os.path.basename(name)
        # File type validation to ensure it's an image
        if not name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            abort(400, description="Unsupported file type.")
        image_path = os.path.join('images', name)
        # Error handling if the file does not exist
        if not os.path.isfile(image_path):
            abort(404, description="Image not found.")
        return f(image_path)
    return wrapper

@app.route('/img/<name>')
@validate_image
def img(name):
    return send_file(name)

if __name__ == '__main__':
    app.run( )