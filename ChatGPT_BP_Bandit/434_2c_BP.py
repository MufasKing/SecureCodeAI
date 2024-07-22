from flask import Flask, request, redirect, url_for

from werkzeug.utils import secure_filename

import os

import base64

import secrets



app = Flask(__name__)



# Configuration

UPLOAD_FOLDER = 'uploads'

ENCODED_FOLDER = 'encoded'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



# Ensure directories exist

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(ENCODED_FOLDER, exist_ok=True)



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['ENCODED_FOLDER'] = ENCODED_FOLDER



def allowed_file(filename):

    """Check if the file has an allowed extension."""

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def generate_random_filename(extension):

    """Generate a secure random filename."""

    return secrets.token_hex(16) + '.' + extension



def upload_image(file):

    """Handle image upload, encoding, and saving."""

    if file and allowed_file(file.filename):

        # Secure the filename

        filename = secure_filename(file.filename)

        # Extract file extension

        file_extension = filename.rsplit('.', 1)[1].lower()

        # Generate a random filename

        random_filename = generate_random_filename(file_extension)

        # Define the full path for the upload

        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], random_filename)

        

        # Save the file to the upload directory
 
        file.save(upload_path)

        

        # Read the file and encode it in base64

        with open(upload_path, 'rb') as image_file:

            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        

        # Write the base64 encoded image to a new file

        encoded_filename = random_filename.rsplit('.', 1)[0] + '.txt'

        encoded_path = os.path.join(app.config['ENCODED_FOLDER'], encoded_filename)

        

        with open(encoded_path, 'w') as encoded_file:

            encoded_file.write(encoded_string)

        

        return encoded_path



@app.route('/upload', methods=['GET', 'POST'])

def upload_file():

    if request.method == 'POST':

        # Check if the post request has the file part

        if 'file' not in request.files:

            return 'No file part'

        file = request.files['file']

        # If user does not select file, browser also submit an empty part without filename

        if file.filename == '':

            return 'No selected file'

        # Process the upload

        encoded_file_path = upload_image(file)

        return f'File successfully uploaded and encoded. Encoded file: {encoded_file_path}'

    

    return '''

    <!doctype html>

    <title>Upload new File</title>

    <h1>Upload new File</h1>

    <form method=post enctype=multipart/form-data>

      <input type=file name=file>

      <input type=submit value=Upload>

    </form>

    '''



if __name__ == '__main__':

    app.run( )