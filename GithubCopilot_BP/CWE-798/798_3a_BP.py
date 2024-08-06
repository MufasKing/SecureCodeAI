from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)

# Database configuration
DB_SERVER = 'localhost'
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'

# Secure configuration
app.config['SECRET_KEY'] = os.urandom(24)

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_SERVER,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        cursor_factory=RealDictCursor
    )
    return conn

def get_server_name():
    return DB_SERVER

def get_database_name():
    return DB_NAME

def get_database_user():
    return DB_USER

def get_database_password():
    return DB_PASSWORD

@app.route('/')
def index():
    return "Welcome to the Secure Web App!"

if __name__ == '__main__':
    app.run( )