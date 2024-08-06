from flask import Flask, request, redirect, url_for, flash

from werkzeug.utils import secure_filename

import os

import magic



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

app.config['ALLOWED_EXTENSIONS'] = {'pdf'}



# Ensure upload folder exists

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



def allowed_file_type(file_path):

    mime = magic.Magic(mime=True)

    file_mime = mime.from_file(file_path)

    # Check if the MIME type is PDF

    return file_mime == 'application/pdf'



@app.route('/', methods=['GET', 'POST'])

def upload_file():

    if request.method == 'POST':

        # Check if the post request has the file part

        if 'file' not in request.files:

            flash('No file part')

            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an

        # empty file without a filename.

        if file.filename == '':

            flash('No selected file')

            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Check if file already exists

            if os.path.exists(file_path):

                flash('File already exists')

                return redirect(request.url)

            # Save file to disk to check its MIME type

            file.save(file_path)

            if not allowed_file_type(file_path):

                os.remove(file_path)  # Remove the file if it's not a PDF

                flash('Invalid file type')

                return redirect(request.url)

            return redirect(url_for('upload_file', filename=filename))

    return '''

    <!doctype html>

    <title>Upload new File</title>

    <h1>Upload new PDF</h1>

    <form method=post enctype=multipart/form-data>

      <input type=file name=file>

      <input type=submit value=Upload>

    </form>

    '''



if __name__ == '__main__':

    app.run( )