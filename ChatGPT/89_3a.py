from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)

# Function to insert a user message into the database
def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS messages (username TEXT, message TEXT)')
    cursor.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))
    conn.commit()
    conn.close()

# Function to get all messages from the database
def get_all_messages_from_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS messages (username TEXT, message TEXT)')
    cursor.execute('SELECT username, message FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return messages

# Route to handle form submissions
@app.route('/post', methods=['POST'])
def post():
    username = request.form.get('username')
    message = request.form.get('message')
    insert_user_message_in_db(username, message)
    return redirect(url_for('main'))

# Route to display the main page with all messages
@app.route('/')
def main():
    messages = get_all_messages_from_db()
    html = '''
    <html>
    <body>
        <h1>Messages</h1>
        <form action="/post" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea><br>
            <input type="submit" value="Post Message">
        </form>
        <hr>
        <h2>Previous Messages:</h2>
        <ul>
            {% for username, message in messages %}
                <li><strong>{{ username }}:</strong> {{ message }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
