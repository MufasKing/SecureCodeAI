<<<<<<< HEAD
from flask import Flask, request, send_file, abort

import os



app = Flask(__name__)



# Ensure that the folder where images are stored is defined and secured

IMAGE_FOLDER = 'path_to_image_folder'



# Function to secure file paths

def secure_file_path(filename):

    # Validate filename to prevent directory traversal attacks

    if '..' in filename or filename.startswith('/'):

        abort(400, "Invalid file path")

    return os.path.join(IMAGE_FOLDER, filename)



@app.route('/img')

def img():

    # Get the 'file' parameter from the URL

    filename = request.args.get('file')



    # Valida le' parameter

    if not filename:

        abort(400, "No file parameter provided")

    

    try:

        # Secure the file path

        file_path = secure_file_path(filename)

        

        # Check if the file exists and is a file (not a directory)

        if not os.path.isfile(file_path):

            abort(404, "File not found")



        # Open the file in read binary mode

        return send_file(file_path, as_attachment=True)



    except Exception as e:

        # Handle any other exceptions

        abort(500, f"An error occurred: {str(e)}")



if __name__ == '__main__':

=======
from flask import Flask, request, send_file, abort

import os



app = Flask(__name__)



# Ensure that the folder where images are stored is defined and secured

IMAGE_FOLDER = 'path_to_image_folder'



# Function to secure file paths

def secure_file_path(filename):

    # Validate filename to prevent directory traversal attacks

    if '..' in filename or filename.startswith('/'):

        abort(400, "Invalid file path")

    return os.path.join(IMAGE_FOLDER, filename)



@app.route('/img')

def img():

    # Get the 'file' parameter from the URL

    filename = request.args.get('file')



    # Validate the 'file' parameter
 
    if not filename:

        abort(400, "No file parameter provided")

    

    try:

        # Secure the file path

        file_path = secure_file_path(filename)

        

        # Check if the file exists and is a file (not a directory)

        if not os.path.isfile(file_path):

            abort(404, "File not found")



        # Open the file in read binary mode

        return send_file(file_path, as_attachment=True)



    except Exception as e:

        # Handle any other exceptions

        abort(500, f"An error occurred: {str(e)}")



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(  )