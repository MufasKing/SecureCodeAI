from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)  # HTTPS support

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

@app.before_request
def session_management():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)  # Set session timeout

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not validate_input(username, password):
            return render_template('login.html', error='Invalid input')

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

def validate_input(username, password):
    username_regex = r'^[\w]{4,20}$'
    password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$'

    if not re.match(username_regex, username):
        return False
    if not re.match(password_regex, password):
        return False
    return True

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create sample user
        password_hash = bcrypt.generate_password_hash('Password123@').decode('utf-8')
        user = User(username='admin', password=password_hash)
        db.session.add(user)
        db.session.commit()

    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')