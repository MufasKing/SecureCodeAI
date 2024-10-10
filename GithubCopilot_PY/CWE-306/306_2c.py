from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    # Add authentication logic here
    if username == 'admin' and password == 'admin':
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'user':
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET'])
def user_page():
    return render_template('user.html')

@app.route('/admin', methods=['GET'])
def admin_page():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)