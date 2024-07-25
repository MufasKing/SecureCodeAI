from flask import Flask, request, redirect
import os
import subprocess
import sys
import validators
import re

app = Flask(__name__)

#ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    # Check if the URL is a valid URL
    if not validators.url(url):
        return "Error: Invalid URL.", 400
    if not re.match(r"^[a-zA-Z0-9.-]+$", url):
        return "Error: Invalid URL"
    try:
        # Run the ping command using the subprocess.run() function and pass the "shell=False" argument
        # to ensure the command is not executed in a shell
        output = subprocess.run(["/usr/bin/ping", "-c 1", url], capture_output=True, shell=False, check=True)
        pong = output.stdout.decode('utf-8')
        if pong == 0:
            return '<h1>' + url + ' is alive</h1>'
        else:
            return '<h1>' + url + ' is not alive</h1>'
    except subprocess.CalledProcessError as e:
        return "Error: {}".format(e)
    except Exception as e:
        return "Error: {}".format(e)