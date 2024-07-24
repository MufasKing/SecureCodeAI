from flask import Flask, request, send_from_directory, jsonify
import mysql.connector
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure MySQL connection
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Save filepath to database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO files (filepath) VALUES (%s)', (filepath,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

@app.route('/download/<int:file_id>', methods=['GET'])
def download_pdf(file_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT filepath FROM files WHERE id = %s', (file_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        filepath = result[0]
        if os.path.exists(filepath):
            return send_from_directory(directory=os.path.dirname(filepath), filename=os.path.basename(filepath))
        else:
            return jsonify({'error': 'File not found'}), 404
    else:
        return jsonify({'error': 'File ID not found'}), 404

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run( )
