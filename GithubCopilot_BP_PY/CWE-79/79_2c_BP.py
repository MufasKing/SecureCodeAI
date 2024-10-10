import logging
from flask import Flask, request, make_response, session, escape
from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask_wtf.csrf import CSRFProtect

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Enable CSRF protection globally for the app
csrf = CSRFProtect(app)

# Configure Jinja2 environment
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Configure logging
logging.basicConfig(level=logging.INFO)

def render_response_from_env(environment):
    try:
        # Get the name parameter from the user request, sanitize input
        name = escape(request.args.get('name', ''))
        
        # Ensure the session is secure
        if 'user_id' not in session:
            raise PermissionError("User not authenticated.")
        
        # Get the template from the environment
        template = environment.get_template('greeting_template.html')
        
        # Render the template with the name parameter from the request
        rendered_template = template.render(name=name)
        
        # Return a response with the rendered template
        return make_response(rendered_template)
    except Exception as e:
        # Log the error
        logging.error(f"Error rendering response: {e}")
        # Return an error response
        return make_response("An error occurred while processing your request.", 500)

@app.route('/')
def home():
    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env)
    # Return the response from the render_response_from_env
    return response

if __name__ == '__main__':
    app.run( )