from flask import Flask, request, render_template, redirect
import os
import requests
import json
from auth import obtain_token, convert_token
import webbrowser


app = Flask(__name__)

@app.route('/')
def show_homepage():
    """Display homepage."""

    #TODO

    return render_template("index.html")


@app.route('/auth-pocket')
def authenticate():
    """Authenticate user's Pocket account."""

    request_token = obtain_token()
    redirect_uri = "http://localhost:3000/auth-confirmed"

    pocket_redirect = "https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s" % (request_token, redirect_uri)

    webbrowser.open(pocket_redirect)

    # converted_token = convert_token(request_token)

    # print "TOKEN:", converted_token
    return render_template("display_converted_token.html")


@app.route('/auth-confirmed')
def confirm_auth():
    """Confirm that the user has authorized Pocket with app, then convert request token into a Pocket access token."""

    return render_template("auth_confirmation.html")


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Heroku provides a random port so saving in a variable
    # PORT = int(os.environ.get("PORT", 5000)) 

    app.run(host="0.0.0.0", port=3000)