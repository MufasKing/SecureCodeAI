from flask import Flask, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secure_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
csrf = CSRFProtect(app)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        # Input Validation and Sanitization
        username = username.strip()
        email = email.strip()
        
        # Check if username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return redirect(url_for('user_exists'))
        
        # Secure Password Hashing
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('registration_successful'))
        except Exception as e:
            app.logger.error(f"Internal Server Error: {str(e)}")
            return redirect(url_for('internal_server_error'))
    
    return redirect(url_for('register'))

@app.route('/registration_successful')
def registration_successful():
    return "Registration Successful!"

@app.route('/user_exists')
def user_exists():
    return "User already exists!"

@app.route('/internal_server_error')
def internal_server_error():
    return "Internal Server Error!"

if __name__ == '__main__':
    db.create_all()
    app.run(ssl_context=('cert.pem', 'key.pem'))