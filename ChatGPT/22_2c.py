from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    # Get the 'file' parameter from the URL
    file_name = request.args.get('file')
    
    if not file_name:
        return "File parameter is missing", 400

    # Define the directory where images are stored
    image_directory = 'path_to_your_image_directory'
    
    # Construct the full file path
    file_path = os.path.join(image_directory, file_name)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File not found", 404

    try:
        # Open the file in read binary mode and send it as a response
        return send_file(file_path, mimetype='image/jpeg')  # Change mimetype if needed
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
