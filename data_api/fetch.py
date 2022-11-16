import requests

POST_TIMEOUT = 1.5

def fetch_tokens(url, limit):
    http_get(url)

def http_get(url):
    r = requests.get(url, timeout=POST_TIMEOUT)
    