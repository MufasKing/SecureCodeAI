from flask import Flask, request, redirect, url_for, send_from_directory, abort
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from flask_talisman import Talisman
from werkzeug.middleware.proxy_fix import ProxyFix
import os
import logging

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.wsgi_app = ProxyFix(app.wsgi_app)
Talisman(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User Authentication Setup
class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user_id):
    user = User()
    user.id = user_id
    return user

# File Upload Handling
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# File Deletion
@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    secure_path = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        return 'File deleted'
    else:
        abort(404)

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found', 404

# CSRF Protection is enabled by default with Flask-WTF when the SECRET_KEY is set

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use adhoc SSL for demonstration purposes