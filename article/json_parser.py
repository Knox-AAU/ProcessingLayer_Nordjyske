import json
from article.article_class import ArticleClass

def get_parsed_articles(file_path):
    data_objs = get_articles_data(file_path)
    parsed_articles = []
    for data_obj in data_objs:
        if is_valid(data_obj):
            parsed_articles.append(parse_article(data_obj))
    return parsed_articles

def is_valid(data):
    if (len(data['paragraphs']) < 2 or data['headline'] == ''):
        return False
    elif ('byline' not in data or data['publication'] == ''):
        return False
    return True

def parse_article(data):
    author_name = data['byline']['name']
    art = ArticleClass(data['headline'], data['publication'], data['paragraphs'], author_name)
    print(art.publisher)
    return art

def get_articles_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['content']['articles']
