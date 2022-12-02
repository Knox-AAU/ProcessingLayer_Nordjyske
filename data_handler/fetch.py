import requests
from exceptions import HttpException

GET_TIMEOUT = 10

def fetch_tokens(api_url, limit, offset):
    tokens = []
    word_ratios = http_get(api_url + 'word-ratios?limit=' + str(limit) + '&offset=' + str(offset))
    for word_ratio in word_ratios:
        for a in range(word_ratio['amount']):
            tokens.append(word_ratio['word'])
    return tokens

def fetch_changeable_categories(api_url):
    ids = []
    categories = http_get(api_url + 'categories')
    for category in categories:
        if category['id'] != 1:
            ids.append(category['id'])
    return ids

def fetch_documents(api_url, limit, offset):
    return http_get(api_url + 'documents?limit=' + str(limit) + '&offset=' + str(offset))

def fetch_word_vecs(api_url, limit, offset, vecs_template):
    all_word_vecs = []
    for doc in fetch_documents(api_url, limit, offset):
        word_vecs = []
        words = http_get(api_url + 'word-ratios/documents/' + str(doc['id']))
        for t_word in vecs_template:
            score = 0
            for db_word in words:
                if t_word == db_word['word']:
                    score = db_word['clusteringScore']
                    break
            word_vecs.append(score)
        all_word_vecs.append({'id': doc['id'], 'vec': word_vecs})
    return all_word_vecs

def fetch_article_count(api_url):
    return http_get(api_url + 'documents/count')

def http_get(url):
    r = requests.get(url, timeout=GET_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Get. Code: ' + str(r.status_code) + ' || Response: ' + r.text)
    else:
        return r.json()
    