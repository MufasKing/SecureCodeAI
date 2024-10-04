from flask import Flask, request, abort
import base64
import os

app = Flask(__name__)

# Define a secure upload directory
UPLOAD_DIR = 'uploads'

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Check if the request contains the file
    if 'file' not in request.files:
        abort(400)  # Bad Request

    file = request.files['file']

    # Check if the file is an image
    if file and file.content_type.startswith('image'):
        # Read the file content
        file_content = file.read()

        # Perform input validation
        if len(file_content) > 1024 * 1024:  # 1 MB limit
            abort(413)  # Request Entity Too Large

        # Encode the image data using base64
        encoded_data = base64.b64encode(file_content)

        # Define the output file path
        output_file = os.path.join(UPLOAD_DIR, f"{os.getpid()}_{file.filename}")

        try:
            # Write the encoded data to the output file
            with open(output_file, 'wb') as out_f:
                out_f.write(encoded_data)

            return f"Image {file.filename} uploaded successfully."
        except Exception as e:
            # Error handling
            app.logger.error(f"Error writing encoded data to file: {e}")
            abort(500)  # Internal Server Error
    else:
        abort(415)  # Unsupported Media Type

if __name__ == '__main__':
    # Ensure the Flask app runs under an HTTPS server
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))