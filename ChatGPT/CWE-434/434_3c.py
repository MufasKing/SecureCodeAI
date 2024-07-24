import os
from flask import Flask, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a real secret key in a production environment

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def file_is_safe_type(filename):
    """
    Check if the uploaded file has a safe extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    """
    Handle the upload of the file.
    """
    if file and file_is_safe_type(file.filename):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return True
    return False

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if upload_file(file):
        flash('File successfully uploaded')
    else:
        flash('File type not allowed')
    
    return redirect(url_for('upload'))

if __name__ == '__main__':
    # Ensure the uploads folder exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run( )
