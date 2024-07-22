<<<<<<< HEAD
from flask import Flask, request, render_template_string, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import InputRequired, Email, Length

from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

csrf = CSRFProtect(app)



# User model

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)



# Registration form

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=80)])

    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=200)])

    first_name = StringField('First Name', validators=[InputRequired(), Length(max=50)])

    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=50)])

    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])

    submit = SubmitField('Register')



@app.route('/register', methods=['GET', 'POST'])

def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data

        password = form.password.data

        first_name = form.first_name.data

        last_name = form.last_name.data

        email = form.email.data

        

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:

            flash('Username already exists. Please choose a different one.', 'error')
 
            return redirect(url_for('register'))

        

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password, first_name=first_name, last_name=last_name, email=email)

        

        try:

            db.session.add(new_user)

            db.session.commit()

            flash('Registration succeeded!', 'success')

            return redirect(url_for('register'))

        except Exception as e:

            db.session.rollback()

            flash('Error occurred: ' + str(e), 'error')

    

    return render_template_string('''

    <!doctype html>

    <html>

        <head>

            <title>Register</title>

        </head>

        <body>

            <h1>Register</h1>

            <form method="POST" action="">

                {{ form.hidden_tag() }}

                <p>{{ form.username.label }}<br>{{ form.username(size=32) }}</p>

                <p>{{ form.password.label }}<br>{{ form.password(size=32) }}</p>

                <p>{{ form.first_name.label }}<br>{{ form.first_name(size=32) }}</p>

                <p>{{ form.last_name.label }}<br>{{ form.last_name(size=32) }}</p>

                <p>{{ form.email.label }}<br>{{ form.email(size=32) }}</p>

                <p>{{ form.submit() }}</p>

            </form>

            {% with messages = get_flashed_messages(with_categories=true) %}

              {% if messages %}

                <ul>

                {% for category, message in messages %}

                  <li class="{{ category }}">{{ message }}</li>

                {% endfor %}

                </ul>

              {% endif %}

            {% endwith %}

        </body>

    </html>

    ''', form=form)



if __name__ == '__main__':

    db.create_all()

=======
from flask import Flask, request, render_template_string, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=200)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password, first_name=first_name, last_name=last_name, email=email)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration succeeded!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()
            flash('Error occurred: ' + str(e), 'error')
    
    return render_template_string('''
    <!doctype html>
    <html>
        <head>
            <title>Register</title>
        </head>
        <body>
            <h1>Register</h1>
            <form method="POST" action="">
                {{ form.hidden_tag() }}
                <p>{{ form.username.label }}<br>{{ form.username(size=32) }}</p>
                <p>{{ form.password.label }}<br>{{ form.password(size=32) }}</p>
                <p>{{ form.first_name.label }}<br>{{ form.first_name(size=32) }}</p>
                <p>{{ form.last_name.label }}<br>{{ form.last_name(size=32) }}</p>
                <p>{{ form.email.label }}<br>{{ form.email(size=32) }}</p>
                <p>{{ form.submit() }}</p>
            </form>
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                <ul>
                {% for category, message in messages %}
                  <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
        </body>
    </html>
    ''', form=form)

if __name__ == '__main__':
    db.create_all()
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)