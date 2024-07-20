from flask import Flask, request, render_template_string

app = Flask(__name__)

def render_response_from_env(env):
    # Get the 'name' parameter from the user request
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no 'name' parameter is provided
    
    # Get the template from the environment (assuming it's a string for simplicity)
    template = env.get('template', '<p>Hello, {{ name }}!</p>')  # Default template if none provided
    
    # Render the template with the 'name' parameter
    rendered_template = render_template_string(template, name=name)
    
    # Return a response with the rendered template
    return rendered_template

@app.route('/')
def home():
    # Define an environment-like dictionary with a template
    env = {
        'template': '<p>Hello, {{ name }}! Welcome to our site.</p>'
    }
    
    # Call the render_response_from_env function with the env variable
    response = render_response_from_env(env)
    
    # Return the response
    return response

if __name__ == '__main__':
    app.run(debug=True)
