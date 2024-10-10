import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 1024 * 1024 * 5  # 5MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_is_safe_type(file_path):
    # Implement file type validation (e.g., using MIME types or file extensions)
    return allowed_file(file_path)

def reset_file_pointer(p):
    p.seek(0)

def check_file_size(p):
    p.seek(0, os.SEEK_END)
    file_size = p.tell()
    reset_file_pointer(p)
    return file_size <= MAX_FILE_SIZE

def detect_malicious_content(p):
    # Implement malicious content detection (placeholder)
    # This should ideally be a more sophisticated check
    reset_file_pointer(p)
    content = p.read()
    reset_file_pointer(p)
    return "malicious" not in content

def upload_file(p, filename):
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    if not file_is_safe_type(filename):
        return "File type is not allowed."
    
    if not check_file_size(p):
        return "File size exceeds the maximum allowed limit."
    
    if not detect_malicious_content(p):
        return "File contains malicious content."
    
    secure_name = secure_filename(filename)
    p.save(os.path.join('uploads', secure_name))
    return f"File {secure_name} uploaded successfully."