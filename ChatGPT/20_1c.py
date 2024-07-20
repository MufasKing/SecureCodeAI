from flask import Flask, request, redirect
import re

app = Flask(__name__)

# Define the regular expression for validation
pattern = re.compile(r'^[\w-]+\.$')

@app.route('/')
def index():
    # Get the target parameter from the query string
    target = request.args.get('target')
    
    # Check if the target parameter is provided
    if target:
        # Match the target against the regular expression
        if pattern.match(target):
            return redirect(target)
        else:
            # If it doesn't match, redirect to the root of the site
            return redirect('/')
    else:
        # If no target is provided, redirect to the root of the site
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
