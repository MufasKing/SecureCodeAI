from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import bcrypt
import os

app = Flask(__name__)

# Secure configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<db_user>:<db_password>@<db_server>/<db_name>'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Function to return database connection details
def get_db_connection():
    return db.engine.connect()

# Functions to return server details (example with dummy data)
def get_server_name():
    return "localhost"

def get_db_name():
    return "my_database"

def get_db_user():
    return "my_user"

def get_db_password():
    return "my_password"

# Password hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Route to create a new user (example)
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not username or not password:
            abort(400)

        # Prevent SQL Injection by using ORM methods
        if User.query.filter_by(username=username).first():
            abort(400, description="User already exists")

        hashed_password = hash_password(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=False)