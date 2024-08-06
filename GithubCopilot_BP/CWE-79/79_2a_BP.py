from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = Flask(__name__)

# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def sanitize_input(input_string):
    """
    Sanitize the input to prevent injection attacks.
    """
    # Basic sanitization. This should be expanded based on the context and expected inputs.
    return input_string.replace('<', '').replace('>', '').replace('"', '').replace("'", '')

def add_security_headers(response):
    """
    Add security headers to the response to improve security.
    """
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

def render_response_from_env(environment):
    """
    Renders a response from the environment using a template and a name parameter from the request.
    """
    # Get the name parameter from the request and sanitize it
    name = sanitize_input(request.args.get('name', ''))
    
    # Get the template from the environment
    template = environment.get_template('greeting.html')
    
    # Render the template with the name parameter
    rendered_template = template.render(name=name)
    
    # Create a response and add security headers
    response = make_response(rendered_template)
    response = add_security_headers(response)
    
    return response

@app.route('/')
def home():
    """
    Home route that renders a response using the environment.
    """
    response = render_response_from_env(env)
    return response

if __name__ == '__main__':
    app.run( )