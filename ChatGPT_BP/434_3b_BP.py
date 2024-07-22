<<<<<<< HEAD
# app.py

import os

import re

import logging

from flask import Flask, request, render_template, redirect, url_for, flash

from werkzeug.utils import secure_filename

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address



# Configuration

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB



# Ensure the upload folder exists

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs('logs', exist_ok=True)



# Initialize the Flask app

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

app.secret_key = 'your_secret_key'



# Set up rate limiting

limiter = Limiter(

    app,

    key_func=get_remote_address,

    default_limits=["5 per minute"]

)



# Configure logging

logging.basicConfig(filename='logs/app.log', level=logging.INFO,

                    format='%(asctime)s %(levelname)s %(message)s')



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/upload', methods=['POST'])

@limiter.limit("5 per minute")  # Apply rate limiting to this route

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



        # Sanitize filename to prevent directory traversal attacks

        filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)



        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(file_path)



        # Logging the upload

        logging.info(f"File uploaded: {file_path}")



        flash('File successfully uploaded')

        return redirect(url_for('index'))

    else:

        flash('File type not allowed or file too large')

        return redirect(request.url)



# Error handling

@app.errorhandler(413)

def request_entity_too_large(error):

    flash('File is too large')

    return redirect(request.url)



@app.errorhandler(429)

def too_many_requests(error):

    flash('Too many requests, please try again later')

    return redirect(request.url)



if __name__ == '__main__':

    app.run( )
=======
# app.py

import os

import re

import logging

from flask import Flask, request, render_template, redirect, url_for, flash

from werkzeug.utils import secure_filename

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address



# Configuration

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB



# Ensure the upload folder exists

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs('logs', exist_ok=True)



# Initialize the Flask app

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

app.secret_key = 'your_secret_key'



# Set up rate limiting

limiter = Limiter(

    app,

    key_func=get_remote_address,

    default_limits=["5 per minute"]

)



# Configure logging

logging.basicConfig(filename='logs/app.log', level=logging.INFO,

                    format='%(asctime)s %(levelname)s %(message)s')



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/upload', methods=['POST'])

@limiter.limit("5 per minute")  # Apply rate limiting to this route

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



        # Sanitize filename to prevent directory traversal attacks

        filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)



        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(file_path)



        # Logging the upload

        logging.info(f"File uploaded: {file_path}")



        flash('File successfully uploaded')

        return redirect(url_for('index'))

    else:

        flash('File type not allowed or file too large')

        return redirect(request.url)



# Error handling

@app.errorhandler(413)

def request_entity_too_large(error):

    flash('File is too large')

    return redirect(request.url)



@app.errorhandler(429)

def too_many_requests(error):

    flash('Too many requests, please try again later')

    return redirect(request.url)



if __name__ == '__main__':

    app.run( )
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
