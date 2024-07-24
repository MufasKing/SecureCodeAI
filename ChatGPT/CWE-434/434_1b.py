from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# Ensure the 'uploads' directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return redirect(url_for('upload_form'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file and file.filename.lower().endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f'File successfully uploaded and saved to {filepath}'
    else:
        return "File is not a PDF"

@app.route('/form')
def upload_form():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Upload PDF</title>
        </head>
        <body>
            <h1>Upload PDF File</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <label for="file">Choose PDF file:</label>
                <input type="file" id="file" name="file" accept=".pdf" required>
                <button type="submit">Upload</button>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run( )
