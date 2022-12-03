import requests
from exceptions import HttpException

DELETE_TIMEOUT = 5

def delete_categories(api_url, ids):
    for id in ids:
        http_delete(f'{api_url}categories/{id}')

def http_delete(url):
    r = requests.delete(url, timeout=DELETE_TIMEOUT)
    if r.status_code != 200:
        raise HttpException(f'Post. Code: {r.status_code} || Response: {r.text}')
    