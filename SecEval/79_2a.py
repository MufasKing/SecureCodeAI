from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader
import os

app = Flask(__name__)
loader = FileSystemLoader( searchpath="templates/" )

env = Environment(
    loader=loader,
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
)

def render_response_from_env(env):
    name = request.args.get('name', '')
    name = escape(name)
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

# CSRF protection
app.config['WTF_CSRF_SECRET_KEY'] = 'secret_key'
app.config['WTF_CSRF_TIME_LIMIT'] = None

# Index page
@app.route('/', methods=["GET", "POST"])
def home():
    return render_response_from_env(env)