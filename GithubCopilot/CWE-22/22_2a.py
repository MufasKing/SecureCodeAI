from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/img')
def img():
    name = request.args.get('name')
    file_path = f'images/{name}'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)