from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Define a function to render a response from an environment
def render_response_from_env(env):
    # Retrieve the 'name' parameter from the request (assuming request.args.get('name') is secure)
    name = request.args.get('name')
    
    # Check if 'name' parameter is provided
    if not name:
        return make_response("Please provide a name parameter.", 400)
    
    # Sanitize the 'name' parameter to prevent potential vulnerabilities
    safe_name = sanitize_input(name)
    
    # Fetch the template using the environment based on the 'name' parameter
    template = env.get_template(f"templates/{safe_name}.html")
    
    # Render the template with the 'name' parameter
    rendered_template = template.render(name=safe_name)
    
    # Return a response containing the rendered template
    return make_response(rendered_template)

# Define a function 'home' that calls render_response_from_env with an environment variable and returns the response
def home():
    # Create a Jinja2 environment with a FileSystemLoader to load templates from the 'templates' directory
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Call the render_response_from_env function with the Jinja2 environment
    response = render_response_from_env(env)
    
    # Return the response
    return response

# Define a function to sanitize input to prevent potential vulnerabilities
def sanitize_input(input_string):
    # Implement sanitization logic here, e.g., using regular expressions
    # This is a placeholder example: replace all non-alphanumeric characters with an empty string
    sanitized_string = ''.join(char for char in input_string if char.isalnum())
    return sanitized_string