from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['WTF_CSRF_SECRET_KEY'] = 'your_csrf_secret_key_here'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Data Management - In-memory user storage
users = {
    'user@example.com': {'password': generate_password_hash('userpassword'), 'role': 'user'},
    'admin@example.com': {'password': generate_password_hash('adminpassword'), 'role': 'admin'}
}

class User(UserMixin):
    def __init__(self, email, role):
        self.id = email
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user = users.get(user_id)
    if user:
        return User(email=user_id, role=user['role'])
    return None

# Form for login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=25)])

# Role-Based Access Control Decorator
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                flash('You do not have access to this page.', 'danger')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/')
@login_required
def index():
    if current_user.role == 'admin':
        return redirect(url_for('admin'))
    return redirect(url_for('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get(form.email.data)
        if user and check_password_hash(user['password'], form.password.data):
            login_user(User(email=form.email.data, role=user['role']))
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/user')
@login_required
@role_required('user')
def user():
    return 'User Page'

@app.route('/admin')
@login_required
@role_required('admin')
def admin():
    return 'Admin Page'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
