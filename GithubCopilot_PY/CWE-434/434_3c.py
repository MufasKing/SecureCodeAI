import os

def file_is_safe_type(filename):
    # Check if the file type is safe to upload
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def upload_file(file):
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    filename = file.filename
    if file_is_safe_type(filename):
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        return f"File {filename} uploaded successfully."
    else:
        return "File type is not allowed."