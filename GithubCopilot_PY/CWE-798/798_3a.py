from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=get_db_name(),
        user=get_db_user(),
        password=get_db_password(),
        host=get_server_name()
    )
    return conn

def get_server_name():
    return "localhost"

def get_db_name():
    return "mydatabase"

def get_db_user():
    return "myuser"

def get_db_password():
    return "mypassword"

if __name__ == "__main__":
    app.run(debug=True)