from flask import Flask, request, render_template, redirect, url_for, flash

from werkzeug.utils import secure_filename

import os



app = Flask(__name__)



# Configuration settings

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file size

SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

app.config['SECRET_KEY'] = SECRET_KEY



# Ensure the upload directory exists

if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)



# Function to check allowed file extensions

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Stub function to validate file type

def file_is_safe_type(file):

    # Implement actual file type checking here

    return True



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/upload', methods=['GET', 'POST'])

def upload_file():

    if request.method == 'POST':

        # Check if the post request has the file part

        if 'file' not in request.files:
 
            flash('No file part')

            return redirect(request.url)



        file = request.files['file']



        # If user does not select a file, browser also

        # submits an empty part without filename

        if file.filename == '':

            flash('No selected file')

            return redirect(request.url)



        if file and allowed_file(file.filename):

            if file_is_safe_type(file):

                filename = secure_filename(file.filename)

                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                

                try:

                    file.save(file_path)

                    flash('File successfully uploaded')

                    return redirect(url_for('index'))

                except Exception as e:

                    flash(f'An error occurred while saving the file: {e}')

                    return redirect(request.url)

            else:

                flash('File type is not allowed')

                return redirect(request.url)

        else:

            flash('File extension is not allowed')

            return redirect(request.url)

    return render_template('upload.html')



@app.errorhandler(413)

def request_entity_too_large(error):

    flash('File is too large')

    return redirect(request.url), 413



if __name__ == '__main__':

    app.run(  )