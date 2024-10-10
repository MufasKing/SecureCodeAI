from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return 'No file part', 400
    file = request.files['pdf_file']
    if file.filename == '':
        return 'No selected file', 400
    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File successfully uploaded', 200
    else:
        return 'Invalid file type', 400

if __name__ == '__main__':
    app.run(debug=True)