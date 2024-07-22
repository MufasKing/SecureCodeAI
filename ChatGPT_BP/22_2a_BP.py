<<<<<<< HEAD
from flask import Flask, send_file, request, abort

import os



app = Flask(__name__)



# Allowed file extensions

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/img', methods=['GET'])

def img():

    # Get the 'name' parameter from the URL

    name = request.args.get('name')



    # Input sanitization: Check if 'name' parameter is provided

    if not name:

        abort(400, description="Missing 'name' parameter")



    # File type validation: Check if the file has an allowed extension

    if not allowed_file(name):

        abort(400, description="Invalid file type")



    # Construct the file path

    file_path = os.path.join('images', name)



    try:

        # Check if the file exists

        if not os.path.isfile(file_path):

            abort(404, description="File not found")



        # Open and send the file

        return send_file(file_path)

    except Exception as e:

        # Error handling: Log the error and return a 500 error

        app.logger.error(f"Error opening file: {e}")

        abort(500, description="Internal server error")



if __name__ == '__main__':

    app.run( )
=======
from flask import Flask, send_file, request, abort

import os



app = Flask(__name__)



# Allowed file extensions

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/img', methods=['GET'])

def img():

    # Get the 'name' parameter from the URL

    name = request.args.get('name')



    # Input sanitization: Check if 'name' parameter is provided

    if not name:

        abort(400, description="Missing 'name' parameter")



    # File type validation: Check if the file has an allowed extension

    if not allowed_file(name):

        abort(400, description="Invalid file type")



    # Construct the file path

    file_path = os.path.join('images', name)



    try:

        # Check if the file exists

        if not os.path.isfile(file_path):

            abort(404, description="File not found")



        # Open and send the file

        return send_file(file_path)

    except Exception as e:

        # Error handling: Log the error and return a 500 error

        app.logger.error(f"Error opening file: {e}")

        abort(500, description="Internal server error")



if __name__ == '__main__':

    app.run(debug=True)
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
