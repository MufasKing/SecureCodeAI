from flask import Flask, request, render_template_string

app = Flask(__name__)

def render_response_from_env(env):
    # Get the name parameter from the user request
    name = request.args.get('name', 'Guest')
    
    # Get the template from the environment
    template = env.get_template('template.html')
    
    # Render the template with the name parameter from the request
    rendered_template = template.render(name=name)
    
    # Return a response with the rendered template
    return rendered_template

@app.route('/')
def home():
    # Assume env is defined somewhere globally or passed to the function
    response = render_response_from_env(env)
    return response

if __name__ == '__main__':
    app.run(debug=True)