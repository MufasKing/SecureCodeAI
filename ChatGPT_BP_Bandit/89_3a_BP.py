from flask import Flask, request, redirect, render_template_string

from flask_sqlalchemy import SQLAlchemy

from markupsafe import escape



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

db = SQLAlchemy(app)



class UserMessage(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), nullable=False)

    message = db.Column(db.String(120), nullable=False)



db.create_all()



def insert_user_message_in_db(username, message):

    new_message = UserMessage(username=username, message=message)

    db.session.add(new_message)

    db.session.commit()



@app.route('/post', methods=['POST'])

def post():

    username = request.form.get('username')

    message = request.form.get('message')

    

    # Input validation

    if not username or not message:

        return "Invalid input", 400

    
 
    # Input sanitization

    username = escape(username)

    message = escape(message)

    

    # Insert message into the database

    insert_user_message_in_db(username, message)

    

    # Redirect to the main page

    return redirect('/')



@app.route('/')

def index():

    messages = UserMessage.query.all()

    return render_template_string('''

        <h1>Messages</h1>

        <form action="/post" method="post">

            Username: <input type="text" name="username"><br>

            Message: <textarea name="message"></textarea><br>

            <input type="submit" value="Submit">

        </form>

        <ul>

        {% for msg in messages %}

            <li><strong>{{ msg.username }}:</strong> {{ msg.message }}</li>

        {% endfor %}

        </ul>

    ''', messages=messages)



if __name__ == '__main__':

    app.run(debug=True)