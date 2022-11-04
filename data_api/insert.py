import requests
from console import print_warning
from exceptions import HttpException

API_URL = 'http://localhost:5501/document-data-api/'

def insert_articles_tokens(articles):
    for art in articles:
        art.id = insert_article(art)
        if art.id == -1:
            break
        insert_content(art)
        insert_tokens(art)

def insert_article(art):
    json_data = [{
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
    if art.publisher != 'Nordjyske Medier':
        print_warning('Article is skipped. Not from Nordjyske Medier. Data: ' + str(json_data))
        return -1
    else:
        return make_post(API_URL+'documents', json_data)[0]

def insert_content(art):
    if len(art.sub_head) == 0:
        json_data = [{
            'documentId': art.id,
            "index": 0,
            'content': art.body_text[0]
        }]
        make_post(API_URL+'document-contents', json_data)
    else:
        json_data = []
        for index, sub_body in enumerate(zip(art.sub_head, art.body_text)):
            json_data.append({
                'documentId': art.id,
                "index": index,
                'subheading': sub_body[0],
                'content': sub_body[1]
            })
        make_post(API_URL+'document-contents', json_data)

def insert_tokens(art):
    json_data = []
    for token in art.tokens:
        if token != '':
            json_data.append({
                'documentId': art.id,
                'word': token,
                'amount': art.tokens[token]['amount'],
                'percent': art.tokens[token]['amount']/art.total_words,
                'rank': art.tokens[token]['rank'],
                'clusteringScore': 0
            })
    make_post(API_URL+'word-ratios', json_data)

def make_post(url, json_data):
    r = requests.post(url, json=json_data, timeout=1.5)
    if r.status_code != 200:
        raise HttpException('Post - code: ' + str(r.status_code) + ' - Data:' + r.text)
    else:
        return r.json()
