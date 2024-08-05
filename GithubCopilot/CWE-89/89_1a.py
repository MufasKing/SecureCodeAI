from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template for the unsubscribe form
form_html = '''
<!doctype html>
<html>
    <body>
        <h2>Unsubscribe Form</h2>
        <form method="POST">
            Email: <input type="email" name="email" required>
            <input type="submit" value="Unsubscribe">
        </form>
        <p>{{ message }}</p>
    </body>
</html>
'''

def unsubscribe(email):
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()
    
    # Check if the email exists in the database
    cursor.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        # Email found, delete it
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        return "You have been unsubscribed."
    else:
        # Email not found
        conn.close()
        return "Email address not found in the database."

@app.route('/', methods=['GET', 'POST'])
def unsubscribe_form():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        message = unsubscribe(email)
    return render_template_string(form_html, message=message)

if __name__ == '__main__':
    app.run(debug=True)