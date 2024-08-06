import re
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def secure_redirect():
    # Regular expression to match the required pattern
    pattern = r'^[a-zA-Z0-9-]+\.'

    # Retrieve the target query parameter value
    target = request.args.get('target', '')

    try:
        # Input Sanitization by escaping special characters
        sanitized_target = re.escape(target)

        # Input Validation to check if the target matches the regular expression
        if re.match(pattern, sanitized_target):
            # Secure Redirect if the target matches the pattern
            return redirect(sanitized_target, code=302)
        else:
            # Redirect to the root of the site if the target does not match the pattern
            return redirect('/', code=302)
    except Exception as e:
        # Error Handling: Log the error and redirect to the root of the site
        app.logger.error(f'Error during redirection: {e}')
        return redirect('/', code=302)

if __name__ == '__main__':
    app.run( )