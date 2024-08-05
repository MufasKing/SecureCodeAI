from flask import Flask, request, redirect, render_template
app = Flask(__name__)

def insert_user_message_in_db(username, message):
    # Placeholder function to simulate database insertion
    pass

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')

@app.route('/')
def display_messages():
    # Placeholder function to simulate fetching messages from the database
    messages = get_all_messages_from_db()
    return render_template('index.html', messages=messages)

def get_all_messages_from_db():
    # Placeholder function to simulate fetching messages from the database
    return [
        {'username': 'user1', 'message': 'Hello, world!'},
        {'username': 'user2', 'message': 'Hi there!'}
    ]

if __name__ == '__main__':
    app.run(debug=True)