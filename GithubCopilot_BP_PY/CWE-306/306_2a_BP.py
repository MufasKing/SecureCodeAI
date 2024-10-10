from flask import Flask, redirect, request, session, abort
from flask_login import LoginManager, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Mock database for demonstration purposes
users = {
    "user": {"password": generate_password_hash("userpass"), "role": "user"},
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"}
}

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

class User:
    def __init__(self, username):
        self.id = username
        self.role = users[username]['role']

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            user_obj = User(username)
            session['user_id'] = user_obj.get_id()
            return redirect('/user')
        return abort(401)
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.route('/user')
@login_required
def user_page():
    if current_user.role == 'admin':
        return redirect('/admin')
    return 'Welcome User!'

@app.route('/admin')
@login_required
def admin_page():
    if current_user.role != 'admin':
        return abort(403)
    return 'Welcome Admin!'

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use adhoc SSL context for demonstration purposes