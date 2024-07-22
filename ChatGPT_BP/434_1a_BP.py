<<<<<<< HEAD
import os

from flask import Flask, request, send_from_directory, abort, jsonify

from werkzeug.utils import secure_filename

import pymysql

import logging



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

app.config['ALLOWED_EXTENSIONS'] = {'pdf'}



# Database configuration

DB_HOST = 'localhost'

DB_USER = 'user'

DB_PASSWORD = 'password'

DB_NAME = 'database'



# Initialize logging

logging.basicConfig(level=logging.INFO)



# Ensure the upload directory exists

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



# Allowed file extension check

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



# Connect to the database

def get_db_connection():

    return pymysql.connect(

        host=DB_HOST,

        user=DB_USER,

        password=DB_PASSWORD,

        database=DB_NAME,

        cursorclass=pymysql.cursors.DictCursor

    )



@app.route('/upload', methods=['POST'])

def upload_pdf():

    # Check if a file part is present

    if 'file' not in request.files:

        return jsonify({'error': 'No file part in the request'}), 400



    file = request.files['file']



    # Check if a file is selected

    if file.filename == '':

        return jsonify({'error': 'No selected file'}), 400



    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)



        try:

            # Save the file

            file.save(file_path)

            logging.info(f"File saved to {file_path}")



            # Save the file path in the database

            connection = get_db_connection()

            with connection.cursor() as cursor:

                sql = "INSERT INTO pdf_files (file_path) VALUES (%s)"

                cursor.execute(sql, (file_path,))

                connection.commit()

                logging.info(f"File path saved in database: {file_path}")

            connection.close()



            return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200



        except Exception as e:

            logging.error(f"Error during file upload: {e}")

            return jsonify({'error': 'Internal server error'}), 500



    return jsonify({'error': 'Invalid file type'}), 400



@app.route('/download/<int:file_id>', methods=['GET'])

def download_pdf(file_id):

    try:

        connection = get_db_connection()

        with connection.cursor() as cursor:

            sql = "SELECT file_path FROM pdf_files WHERE id = %s"

            cursor.execute(sql, (file_id,))

            result = cursor.fetchone()



            if result is None:

                connection.close()

                return jsonify({'error': 'File not found'}), 404



            file_path = result['file_path']

            connection.close()



            # Ensure the file path is valid and within the uploads folder

            if os.path.isfile(file_path) and os.path.dirname(file_path) == app.config['UPLOAD_FOLDER']:

                return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(file_path), as_attachment=True)



            return jsonify({'error': 'File not found'}), 404



    except Exception as e:

        logging.error(f"Error during file download: {e}")

        return jsonify({'error': 'Internal server error'}), 500



if __name__ == '__main__':

    # Run the Flask app

    app.run( )
=======
import os

from flask import Flask, request, send_from_directory, abort, jsonify

from werkzeug.utils import secure_filename

import pymysql

import logging



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

app.config['ALLOWED_EXTENSIONS'] = {'pdf'}



# Database configuration

DB_HOST = 'localhost'

DB_USER = 'user'

DB_PASSWORD = 'password'

DB_NAME = 'database'



# Initialize logging

logging.basicConfig(level=logging.INFO)



# Ensure the upload directory exists

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



# Allowed file extension check

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



# Connect to the database

def get_db_connection():

    return pymysql.connect(

        host=DB_HOST,

        user=DB_USER,

        password=DB_PASSWORD,

        database=DB_NAME,

        cursorclass=pymysql.cursors.DictCursor

    )



@app.route('/upload', methods=['POST'])

def upload_pdf():

    # Check if a file part is present

    if 'file' not in request.files:

        return jsonify({'error': 'No file part in the request'}), 400



    file = request.files['file']



    # Check if a file is selected

    if file.filename == '':

        return jsonify({'error': 'No selected file'}), 400



    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)



        try:

            # Save the file

            file.save(file_path)

            logging.info(f"File saved to {file_path}")



            # Save the file path in the database

            connection = get_db_connection()

            with connection.cursor() as cursor:

                sql = "INSERT INTO pdf_files (file_path) VALUES (%s)"

                cursor.execute(sql, (file_path,))

                connection.commit()

                logging.info(f"File path saved in database: {file_path}")

            connection.close()



            return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200



        except Exception as e:

            logging.error(f"Error during file upload: {e}")

            return jsonify({'error': 'Internal server error'}), 500



    return jsonify({'error': 'Invalid file type'}), 400



@app.route('/download/<int:file_id>', methods=['GET'])

def download_pdf(file_id):

    try:

        connection = get_db_connection()

        with connection.cursor() as cursor:

            sql = "SELECT file_path FROM pdf_files WHERE id = %s"

            cursor.execute(sql, (file_id,))

            result = cursor.fetchone()



            if result is None:

                connection.close()

                return jsonify({'error': 'File not found'}), 404



            file_path = result['file_path']

            connection.close()



            # Ensure the file path is valid and within the uploads folder

            if os.path.isfile(file_path) and os.path.dirname(file_path) == app.config['UPLOAD_FOLDER']:

                return send_from_directory(app.config['UPLOAD_FOLDER'], os.path.basename(file_path), as_attachment=True)



            return jsonify({'error': 'File not found'}), 404



    except Exception as e:

        logging.error(f"Error during file download: {e}")

        return jsonify({'error': 'Internal server error'}), 500



if __name__ == '__main__':

    # Run the Flask app

    app.run(debug=True)
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
