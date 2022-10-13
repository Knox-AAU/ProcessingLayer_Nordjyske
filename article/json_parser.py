import json
from article.article_class import ArticleClass

def get_parsed_articles(file_path):
    data_objs = get_articles_data(file_path)
    parsed_articles = 
    for data_obj in data_objs:
        if is_valid(data_obj):
            parsed_articles.append(parse_article(data_obj))
    return parsed_articles

def is_valid(data):
    if (len(data['paragraphs']) > 1 and data['headline'] != '' and 'byline' in data and data['publication'] != ''):
        return True
    return False

def parse_article(data):
    par_art = ArticleClass(data['headline'], data['publication'], data['byline']['name'], data['paragraphs'])
    return par_art

def get_articles_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['content']['articles']
