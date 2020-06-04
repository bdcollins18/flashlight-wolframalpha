import requests
from urllib import quote
import webbrowser

api_url = "http://api.wolframalpha.com/v2/result"
appid_file = open("appid.txt", "r")
appid = appid_file.read()
appid_file.close()
params = {"appid": appid}


def results(fields, original_query):
    input_string = fields["~input"]
    params["i"] = input_string
    r = requests.get(url=api_url, params=params)

    return {
        "title": "Wolfram Alpha",
        "html": r.text,
        "webview_transparent_background": True,
        "run_args": [input_string]
    }

site_url = "https://www.wolframalpha.com/input/?i="

def run(input_string) :
    webbrowser.open(site_url + quote(input_string))