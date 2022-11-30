import requests
from exceptions import HttpException

PUT_TIMEOUT = 5

def update_word_relevance(api_url):
    print('Updating word relevance (tfidf)...')
    http_put_no_args(api_url + 'tf-idf/update')

def update_document_category(api_url, topics):
    for topic in topics:
        data = {
            'id': topic['id'],
            'categoryId': topic['topic']
        }
        http_put(api_url + 'documents', data)

def http_put_no_args(url):
    r = requests.put(url, timeout=PUT_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Post. Code: ' + str(r.status_code) + '|| Response: ' + r.text)
    else:
        return r.text

def http_put(url, json_data):
    r = requests.put(url, json=json_data, timeout=PUT_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Post. Code: ' + str(r.status_code) + '|| Response: ' + r.text)
    else:
        return r.text


