from flask import Flask, send_from_directory, abort, request, jsonify

import os



app = Flask(__name__)



# Configuration

IMAGE_FOLDER = 'images'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



# Helper function to check allowed file extensions

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Decorator for route

@app.route('/images/<path:filename>', methods=['GET'])

def get_image(filename):

    try:

        # Directory Traversal Protection

        if '..' in filename or filename.startswith('/'):

            abort(400, description="Bad request: Invalid file path.")

        
 
        # Check file extension

        if not allowed_file(filename):

            abort(400, description="Bad request: File type not allowed.")

        

        # Construct the full file path

        file_path = os.path.join(IMAGE_FOLDER, filename)

        

        # Check if file exists

        if not os.path.exists(file_path):

            abort(404, description="File not found.")

        

        # Send the file

        return send_from_directory(IMAGE_FOLDER, filename)

    

    except Exception as e:

        # Error handling

        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':

    # Run the Flask app

    app.run(debug=True)