import requests
from exceptions import HttpException

DELETE_TIMEOUT = 5

def delete_categories(api_url, ids):
    for id in ids:
        http_delete(api_url + 'categories/' + str(id))

def http_delete(url):
    r = requests.delete(url, timeout=DELETE_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Post. Code: ' + str(r.status_code) + ' || Response: ' + r.text)
    