from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/img')
def img():
    file_name = request.args.get('file')
    if file_name:
        try:
            return send_file(file_name, mimetype='image/jpeg')
        except FileNotFoundError:
            return "File not found", 404
    else:
        return "No file specified", 400

if __name__ == '__main__':
    app.run(debug=True)