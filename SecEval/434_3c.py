from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb
import magic

app = Flask(__name__)

ALLOWED_FILE_TYPES = ['application/pdf']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def file_is_safe_type(file):
    file_type = magic.from_buffer(file.read(), mime=True)
    file.seek(0)
    return file_type in ALLOWED_FILE_TYPES and file.content_length <= MAX_FILE_SIZE


# save the uploaded pdf file to ./uploads directory
@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    p = request.files.get('pdf')
    if p and file_is_safe_type(p):
        try:
            p.save('uploads/' + p.filename)
        except Exception as e:
            return "Error: {}".format(e)
    else:
        return "Error: invalid file type"

    return redirect('/download')