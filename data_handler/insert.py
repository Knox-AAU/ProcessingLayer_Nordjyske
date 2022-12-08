import requests
from exceptions import HttpException

POST_TIMEOUT = 1.5
HEADLINE_SCALAR = 1.5
SUBHEADER_SCALAR = 1.25

def insert_articles_tokens(articles, api_url):
    for art in articles:
        # vvv get the first id. Only one article is inserted so only one id will be returned
        art.id = http_post(api_url+'documents', make_article_json(art))[0]
        http_post(api_url+'document-contents', make_content_json(art))
        http_post(api_url+'word-ratios', make_tokens_json(art))

def insert_category_amount(api_url, n_clusters):
    for i in range(1, n_clusters+1):
        http_post(api_url+'categories?name=noName'+str(i), '')

def insert_nearest_arts(arts, api_url):
    nearest_docs = []
    for nearest in arts['nearest']:
        similarity_data = {
            'mainDocumentId': arts['art_id'],
            'similarDocumentId': nearest['id'],
            'similarity': nearest['dist']
        }
        nearest_docs.append(similarity_data)
    http_post(api_url+'similar-documents', nearest_docs)

def make_article_json(art):
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

def make_content_json(art):
    if len(art.sub_head) == 0:
        return [{
            'documentId': art.id,
            'index': 0,
            'content': art.body_text[0]
        }]
    else:
        json_data = []
        for index, sub_body in enumerate(zip(art.sub_head, art.body_text)):
            if (sub_body[0] != '' and sub_body[1] != ''):
                json_data.append({
                    'documentId': art.id,
                    'index': index,
                    'subheading': sub_body[0],
                    'content': sub_body[1]
                })
        return json_data

def make_tokens_json(art):
    def get_score(amount, rank):
        if rank == 1:
            return amount*HEADLINE_SCALAR
        elif rank == 2:
            return amount*SUBHEADER_SCALAR
        elif rank == 3:
            return amount

    json_data = []
    total_amount = art.tokens.get_total_amount()
    for token in art.tokens:
        if token != '':
            amount = art.tokens[token]['amount']
            rank = art.tokens[token]['rank']
            json_data.append({
                'documentId': art.id,
                'word': token,
                'amount': amount,
                'percent': amount/total_amount,
                'rank': rank,
                'clusteringScore': get_score(amount, rank)
            })
    return json_data

def http_post(url, json_data):
    r = requests.post(url, json=json_data, timeout=POST_TIMEOUT)
    if r.status_code not in (200, 204):
        data = f'|| Response: {r.text} || Data: {json_data}'
        raise HttpException(f'Post. Code: {r.status_code}{data}')
    else:
        if r.text != '':
            return r.json()
