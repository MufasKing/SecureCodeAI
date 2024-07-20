from flask import Flask, request, jsonify, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Regexp
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
import bcrypt
import logging
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Setup database connection
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

# Define a registration form with CSRF protection
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[
        InputRequired(), 
        Length(min=8),
        Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message="Password must contain at least one letter and one number.")
    ])

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Generate salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        try:
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                conn.commit()
            logging.info(f"User {username} successfully registered.")
            return jsonify(message="User registered successfully."), 201
        except sqlite3.IntegrityError:
            logging.error(f"User {username} already exists.")
            return jsonify(error="User already exists."), 400
    return render_template_string('''
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username }}
        {{ form.password.label }} {{ form.password }}
        <input type="submit" value="Register">
    </form>
    ''', form=form)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="ratelimit exceeded: %s" % e.description), 429

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad request: %s" % e.description), 400

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal server error: %s" % e.description), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Not found: %s" % e.description), 404

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # For HTTPS use adhoc SSL context for testing