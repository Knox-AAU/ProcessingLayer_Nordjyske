import requests
from exceptions import HttpException

GET_TIMEOUT = 10

def fetch_tokens(api_url, limit, offset):
    tokens = []
    word_ratios = http_get(f'{api_url}word-ratios?limit={limit}&offset={offset}')
    for word_ratio in word_ratios:
        for a in range(word_ratio['amount']):
            tokens.append(word_ratio['word'])
    return tokens

def fetch_editable_categories(api_url):
    ids = []
    categories = http_get(api_url + 'categories')
    for category in categories:
        if category['id'] != 1:
            ids.append(category['id'])
    return ids

def fetch_word_vecs(api_url, limit, offset, vecs_template):
    all_word_vecs = []
    documents = http_get(f'{api_url}documents?limit={limit}&offset={offset}')
    for doc in documents:
        word_vecs = []
        tokens = http_get(f'{api_url}word-ratios/documents/' + str(doc['id']))
        for tem_word in vecs_template:
            score = 0
            for token in tokens:
                if tem_word == token['word']:
                    score = token['clusteringScore']
                    break
            word_vecs.append(score)
        all_word_vecs.append({'id': doc['id'], 'vec': word_vecs})
    return all_word_vecs

def fetch_article_count(api_url):
    return http_get(api_url + 'documents/count')

def http_get(url):
    r = requests.get(url, timeout=GET_TIMEOUT)
    if r.status_code != 200:
        raise HttpException(f'Get. Code: {r.status_code} || Response: {r.text}')
    else:
        return r.json()
    