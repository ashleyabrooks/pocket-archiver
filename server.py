from flask import Flask, request, render_template, redirect
import os
import requests
import json


app = Flask(__name__)

@app.route('/')
def show_homepage():
  """Display homepage."""

  return render_template("index.html")

def authenticate():
    """Authenticate user's Pocket account."""

    pass


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Heroku provides a random port so saving in a variable
    # PORT = int(os.environ.get("PORT", 5000)) 

    app.run(host="0.0.0.0", port=3000)