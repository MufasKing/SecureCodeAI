from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/images/<filename>')
def get_image(filename):
    images_folder = 'images'
    file_path = os.path.join(images_folder, filename)
    
    if os.path.exists(file_path):
        return send_from_directory(images_folder, filename)
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(debug=True)