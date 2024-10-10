from flask import Flask, request, redirect, url_for, flash, abort

from werkzeug.utils import secure_filename

import os

import logging

from logging.handlers import RotatingFileHandler

from functools import wraps

import time



# Configuration

UPLOAD_FOLDER = '/path/to/the/uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

MAX_FILE_SIZE = 1024 * 1024 * 2  # 2MB



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE



# Setup logging

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)

handler.setLevel(logging.INFO)

app.logger.addHandler(handler)



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def rate_limit(max_per_second):

    min_interval = 1.0 / float(max_per_second)

    def decorate(func):

        last_called = [0.0]

        @wraps(func)

        def rate_limited_function(*args, **kwargs):

            elapsed = time.clock() - last_called[0]

            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:

                time.sleep(left_to_wait)

            last_called[0] = time.clock()

            return func(*args, **kwargs)

        return rate_limited_function

    return decorate



@app.route('/upload', methods=['POST'])

@rate_limit(5)  # Limit to 5 requests per second

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

        try:

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            app.logger.info(f"File uploaded: {filename}")

            return redirect(url_for('uploaded_file', filename=filename))

        except Exception as e:

            app.logger.error(f"Error saving file: {str(e)}")

            abort(500)

    else:

        flash('File type not allowed')

        return redirect(request.url)



@app.route('/uploads/<filename>')

def uploaded_file(filename):

    # Implement secure file retrieval

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == '__main__':

    app.run( )