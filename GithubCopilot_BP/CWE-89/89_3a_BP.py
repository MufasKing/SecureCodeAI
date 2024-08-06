from flask import Flask, request, redirect, render_template_string
import html
import sqlite3

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    # Secure Database Interaction
    # Use parameterized queries to avoid SQL Injection
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    connection.commit()
    connection.close()

@app.route('/post', methods=['POST'])
def post():
    # Input Validation and Sanitization
    username = request.form.get('username', '')
    message = request.form.get('message', '')
    
    # Basic sanitization
    username = html.escape(username.strip())
    message = html.escape(message.strip())
    
    # Further validation can be added here based on requirements
    
    # Insert the sanitized and validated input into the database
    insert_user_message_in_db(username, message)
    
    # URL Redirection to the main page
    return redirect('/')

@app.route('/')
def main_page():
    # Secure Database Interaction
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT username, message FROM messages")
    messages = cursor.fetchall()
    connection.close()
    
    # HTML Rendering with escaping to prevent XSS
    # Note: For better security and separation of concerns, use a template engine like Jinja2
    html_content = '<h1>Messages</h1>'
    for username, message in messages:
        html_content += f'<p><b>{html.escape(username)}:</b> {html.escape(message)}</p>'
    
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run( )