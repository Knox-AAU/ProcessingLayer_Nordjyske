import requests
from exceptions import HttpException

API_URL = 'http://localhost:5501/document-data-api/'
POST_TIMEOUT = 1.5

def insert_articles_tokens(articles):
    for art in articles:
        art.id = make_post(API_URL+'documents', get_article_json(art))[0] # get the first id. Only one article is inserted so only one id will be returned
        make_post(API_URL+'document-contents', get_content_json(art))
        make_post(API_URL+'word-ratios', get_tokens_json(art))

def get_article_json(art):
    return [{
        'sourceId': 1,
        'categoryId': 1,
        'title': art.headline,
        'publication': art.publication,
        'path': art.path,
        'date': art.published_at,
        'author': art.author_name,
        'totalWords': art.total_words,
        'uniqueWords': len(art.tokens)
    }]

def get_content_json(art):
    if len(art.sub_head) == 0:
        return [{
            'documentId': art.id,
            'index': 0,
            'content': art.body_text[0]
        }]
    else:
        json_data = []
        for index, sub_body in enumerate(zip(art.sub_head, art.body_text)):
            json_data.append({
                'documentId': art.id,
                'index': index,
                'subheading': sub_body[0],
                'content': sub_body[1]
            })
        return json_data

def get_tokens_json(art):
    json_data = []
    for token in art.tokens:
        if token != '':
            json_data.append({
                'documentId': art.id,
                'word': token,
                'amount': art.tokens[token]['amount'],
                'percent': art.tokens[token]['amount']/len(art.tokens),
                'rank': art.tokens[token]['rank'],
                'clusteringScore': 0
            })
    return json_data

def make_post(url, json_data):
    r = requests.post(url, json=json_data, timeout=POST_TIMEOUT)
    if r.status_code != 200:
        data = '|| Response: ' + r.text + ' || Data: ' + str(json_data)
        raise HttpException('Post. Code: ' + str(r.status_code) + data)
    else:
        return r.json()
