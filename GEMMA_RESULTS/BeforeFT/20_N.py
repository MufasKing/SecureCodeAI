import re
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/<target>')
def redirect_to_target(target):
if re.match(r'https?://example.com/', target):
return redirect(target)
else:
return redirect(url_for('index'))

if __name__ == '__main__':
app.run(debug=True)