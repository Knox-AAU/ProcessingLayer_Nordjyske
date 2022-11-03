import requests
from console import print_warning
from exceptions import HttpException

API_URL = 'http://localhost:5501/document-data-api/'

def insert_articles_tokens(articles):
    for art in articles:
        make_post(art)

def make_post(art):
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
        print_warning('Article is skipped. Not form Nordjyske Medier. Data: ' + str(json_data))
        return

    r = requests.post(API_URL+'documents', json=json_data, timeout=1.5)
    if r.status_code != 200:
        raise HttpException('Post - code: ' + str(r.status_code) + ' - Data:' + r.text)
