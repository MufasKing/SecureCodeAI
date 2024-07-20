from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(200), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

def insert_user_message_in_db(username, message):
    """Inserts a message into the database."""
    new_message = Message(username=username, message=message)
    db.session.add(new_message)
    db.session.commit()

@app.route('/')
def index():
    """Displays all messages."""
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post_message():
    """Handles posting a new message."""
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        insert_user_message_in_db(username, message)
    
    return redirect('/')

# Templates should be placed in a folder named 'templates'
# Create 'templates/index.html' with the following content:
"""
<!DOCTYPE html>
<html>
<head>
    <title>Messages</title>
</head>
<body>
    <h1>Messages</h1>
    <form action="/post" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <input type="submit" value="Post Message">
    </form>
    <ul>
        {% for msg in messages %}
            <li><strong>{{ msg.username }}:</strong> {{ msg.message }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
