from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    # Input Validation
    file_name = request.args.get('file')
    if not file_name:
        return abort(400, description="No file specified")

    # Secure File Path
    # Ensure the file path is within a specific directory to prevent directory traversal attacks
    base_directory = os.path.abspath("/path/to/your/images")
    secure_path = os.path.join(base_directory, file_name)
    secure_path = os.path.abspath(secure_path)

    if not secure_path.startswith(base_directory):
        return abort(403, description="Access denied")

    # Error Handling
    try:
        # File Contents Retrieval
        if os.path.exists(secure_path) and os.path.isfile(secure_path):
            # Response Handling
            return send_file(secure_path, as_attachment=True)
        else:
            return abort(404, description="File not found")
    except Exception as e:
        return abort(500, description=str(e))

if __name__ == '__main__':
    app.run( )