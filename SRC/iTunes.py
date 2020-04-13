import requests
import json

def getFromiTunes(path,queryParams=dict()):
    url = f"https://itunes.apple.com{path}"
    res = requests.get(url, params=queryParams)
    return res.json()