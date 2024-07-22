<<<<<<< HEAD
from flask import Flask, request, redirect, render_template, session, flash, url_for

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField

from wtforms.validators import DataRequired, Length

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from itsdangerous import URLSafeTimedSerializer

import sqlite3

import html



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

app.config['WTF_CSRF_SECRET_KEY'] = 'your_csrf_secret_key_here'



# Initialize rate limiter

limiter = Limiter(

    get_remote_address,

    app=app,

    default_limits=["200 per day", "50 per hour"]

)



# CSRF protection setup

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])



class MessageForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(max=50)])

    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])

    submit = SubmitField('Submit')

 

def insert_user_message_in_db(username, message):

    # Use parameterized queries to prevent SQL injection

    conn = sqlite3.connect('messages.db')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))

    conn.commit()

    conn.close()



@app.route('/', methods=['GET', 'POST'])

@limiter.limit("10 per minute")

def post():

    form = MessageForm()

    if form.validate_on_submit():

        username = html.escape(form.username.data)

        message = html.escape(form.message.data)

        

        insert_user_message_in_db(username, message)

        flash('Message submitted successfully!', 'success')

        return redirect(url_for('post'))

    

    return render_template('index.html', form=form)



@app.errorhandler(429)

def ratelimit_handler(e):

    return "You have been rate limited. Please try again later.", 429



if __name__ == '__main__':

=======
from flask import Flask, request, redirect, render_template, session, flash, url_for

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField

from wtforms.validators import DataRequired, Length

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from itsdangerous import URLSafeTimedSerializer

import sqlite3

import html



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

app.config['WTF_CSRF_SECRET_KEY'] = 'your_csrf_secret_key_here'



# Initialize rate limiter

limiter = Limiter(

    get_remote_address,

    app=app,

    default_limits=["200 per day", "50 per hour"]

)



# CSRF protection setup

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])



class MessageForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(max=50)])

    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])

    submit = SubmitField('Submit')


 
def insert_user_message_in_db(username, message):

    # Use parameterized queries to prevent SQL injection

    conn = sqlite3.connect('messages.db')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))

    conn.commit()

    conn.close()



@app.route('/', methods=['GET', 'POST'])

@limiter.limit("10 per minute")

def post():

    form = MessageForm()

    if form.validate_on_submit():

        username = html.escape(form.username.data)

        message = html.escape(form.message.data)

        

        insert_user_message_in_db(username, message)

        flash('Message submitted successfully!', 'success')

        return redirect(url_for('post'))

    

    return render_template('index.html', form=form)



@app.errorhandler(429)

def ratelimit_handler(e):

    return "You have been rate limited. Please try again later.", 429



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)