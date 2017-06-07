import requests

def get(URL, **params):
    res = requests.get(URL.format(**params))
    return res.content, res.status_code
