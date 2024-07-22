# app.py

from flask import Flask, request, redirect, render_template, flash, url_for

from werkzeug.utils import secure_filename

import os



app = Flask(__name__)

app.secret_key = 'supersecretkey'  # Required for flash messages

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = {'pdf'}



if not os.path.exists(app.config['UPLOAD_FOLDER']):

    os.makedirs(app.config['UPLOAD_FOLDER'])



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route('/')

def index():

    return render_template('upload.html')



@app.route('/upload', methods=['POST'])

def upload_file():

    if 'file' not in request.files:

        flash('No file part')

        return redirect(request.url)



    file = request.files['file']



    if file.filename == '':

        flash('No selected file')

        return redirect(request.url)



    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)



        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if os.path.exists(file_path):

            flash('File already exists')

            return redirect(request.url)



        file.save(file_path)

        flash('File successfully uploaded')

        return redirect(url_for('index'))

    else:

        flash('Invalid file type')

        return redirect(request.url)



if __name__ == '__main__':

    app.run(debug=True)