import os

import werkzeug.utils

import pyclamd

from flask import Flask, request, flash

from werkzeug.utils import secure_filename



# Define allowed extensions and maximum file size (e.g., 2MB)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB



# Create an uploads directory if it doesn't exist

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE



# Function to check if the file has an allowed extension

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Function to detect malicious content using ClamAV

def detect_malware(filepath):

    try:

        cd = pyclamd.ClamdAgnostic()

        if cd.ping():

            scan_result = cd.scan_file(filepath)

            if scan_result:

                return True  # Malware detected

        return False

    except pyclamd.ConnectionError:

        print("Error: Unable to connect to ClamAV daemon.")

        return False



# Function to handle file uploads

@app.route('/upload', methods=['POST'])

def upload_file():

    if 'file' not in request.files:

        flash('No file part')

        return "No file part"



    file = request.files['file']



    # If no file is selected

    if file.filename == '':

        flash('No selected file')

        return "No selected file"



    # Check if file is allowed

    if file and allowed_file(file.filename):

        # Secure the filename

        filename = secure_filename(file.filename)



        # Save the file temporarily to scan for malware

        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(temp_path)



        # Check for malware

        if detect_malware(temp_path):

            os.remove(temp_path)

            return "Malicious file detected!"



        # Check the file size

        file.seek(0, os.SEEK_END)

        file_size = file.tell()

        file.seek(0)  # Reset the file pointer



        if file_size > MAX_FILE_SIZE:

            os.remove(temp_path)

            return "File size exceeds limit!"



        # Move the file to the permanent location

        final_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        os.rename(temp_path, final_path)



        return f"File {filename} uploaded successfully!"



    return "File type not allowed!"



if __name__ == '__main__':

    app.run(  )