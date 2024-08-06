import os

import mysql.connector

from werkzeug.utils import secure_filename

from flask import Flask, request, send_from_directory



app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'pdf'}



# Database configuration

db_config = {

    'user': 'your_db_user',

    'password': 'your_db_password',

    'host': 'localhost',

    'database': 'your_database_name',

    'raise_on_warnings': True

}



# Ensure the upload folder exists

os.makedirs(UPLOAD_FOLDER, exist_ok=True)



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def save_file_path_to_db(filepath):

    try:

        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()

        query = "INSERT INTO pdf_files (filepath) VALUES (%s)"

        cursor.execute(query, (filepath,))

        conn.commit()

    except mysql.connector.Error as err:

        print(f"Error: {err}")

    finally:

        cursor.close()

        conn.close()



@app.route('/upload', methods=['POST'])

def upload_pdf():

    if 'file' not in request.files:

        return "No file part", 400

    file = request.files['file']

    if file.filename == '':

        return "No selected file", 400

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        filepath = os.path.join(UPLOAD_FOLDER, filename)

        try:

            file.save(filepath)

            save_file_path_to_db(filepath)

            return "File successfully uploaded", 200

        except Exception as e:

            return f"An error occurred: {e}", 500

    else:

        return "File type not allowed", 400



@app.route('/downloads/<filename>')

def download_pdf(filename):

    filename = secure_filename(filename)

    try:

        return send_from_directory(UPLOAD_FOLDER, filename)

    except Exception as e:

        return f"An error occurred: {e}", 500



if __name__ == '__main__':

    app.run( )