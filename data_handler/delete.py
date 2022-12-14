import requests
from exceptions import HttpException

DELETE_TIMEOUT = 5

def delete_categories(api_url, ids):
    for cat_id in ids:
        http_delete(f'{api_url}categories/{cat_id}')

def delete_nearest_arts(api_url):
    http_delete(api_url + 'similar-documents/delete-all/')

def http_delete(url):
    r = requests.delete(url, timeout=DELETE_TIMEOUT)
    if r.status_code not in (200, 204):
        raise HttpException(f'Post. Code: {r.status_code} || Response: {r.text}')
