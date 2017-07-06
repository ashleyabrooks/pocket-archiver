import requests


def obtain_token():
    """Obtains and returns a request token."""

    # TODO

    url = "https://getpocket.com/v3/oauth/request"
    consumer_key = "68610-1a3e291e634b6401538c0fd2"
    redirect_uri = ""

    headers = { 
        "Host": "getpocket.com",
        "Content-Type": "application/json; charset=UTF-8",
        "X-Accept": "application/json",
    }

    data = {
        "consumer_key": consumer_key,
        "redirect_uri": redirect_uri,
    }

    r = requests.post(url, headers, data)

    token = r["code"]

    return token