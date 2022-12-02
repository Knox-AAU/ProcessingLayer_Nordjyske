import requests
from exceptions import HttpException

PUT_TIMEOUT = 5

def update_word_relevance(api_url):
    print('Updating word relevance (tfidf)...')
    http_put_no_args(api_url + 'tf-idf/update')

def update_document_category(api_url, topic):
    data = {
        'documentId': topic['id'],
        'categoryId': topic['category']
    }
    http_put(api_url + 'documents/category', data)

def http_put_no_args(url):
    r = requests.put(url, timeout=PUT_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Put. Code: ' + str(r.status_code) + '|| Response: ' + r.text)
    else:
        return r.text

def http_put(url, json_data):
    r = requests.put(url, json=json_data, timeout=PUT_TIMEOUT)
    if r.status_code != 200:
        data = '|| Response: ' + r.text + ' || Data: ' + str(json_data)
        raise HttpException('Put. Code: ' + str(r.status_code) + data)
    else:
        return r.text
