import requests

DATA = {
    "consumer_key": "68610-1a3e291e634b6401538c0fd2",
    "redirect_uri": "http://localhost:3000/",
}

HEADERS = { 
    "Host": "getpocket.com",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Accept": "application/json",
}


def obtain_token():
    """Obtains and returns a request token."""

    url = "https://getpocket.com/v3/oauth/request"

    r = requests.post(url, DATA, HEADERS)

    return r.text[5:]


def convert_token(request_token):
    """Converts request token into a Pocket access token."""

    # TODO - DRY

    url = "https://getpocket.com/v3/oauth/authorize"

    r = requests.post(url, DATA, HEADERS)

    print r.text




