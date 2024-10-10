from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    # Placeholder function to simulate database insertion
    pass

def get_all_messages_from_db():
    # Placeholder function to simulate retrieving messages from the database
    return [
        {"username": "Alice", "message": "Hello, world!"},
        {"username": "Bob", "message": "Hi, Alice!"}
    ]

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')

@app.route('/')
def display_messages():
    messages = get_all_messages_from_db()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)