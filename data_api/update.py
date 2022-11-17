import requests
from exceptions import HttpException
from console import print_all_done

def update_word_relevance(api_url):
    print('Updating word relevance (tfidf)...')
    http_put_no_args(api_url + 'tf-idf/update')
    print_all_done()

def http_put_no_args(url):
    r = requests.put(url)
    if r.status_code != 200:
        raise HttpException('Post. Code: ' + str(r.status_code) + '|| Response: ' + r.text)
    else:
        return r.text
