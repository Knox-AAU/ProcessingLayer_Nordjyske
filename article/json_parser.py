import json
import re
import os
from article.article_class import ArticleClass

def get_parsed_articles(file_path):
    data_objs = get_articles_data(file_path)
    parsed_articles = []
    for data_obj in data_objs:
        if is_valid(data_obj):
            parsed_articles.append(parse_article(data_obj, file_path))
    return parsed_articles

def is_valid(data):
    if (len(data['paragraphs']) < 2 or data['headline'] == ''):
        return False
    elif ('byline' not in data or data['publication'] == ''):
        return False
    return True

def parse_article(data, file_path):
    art = ArticleClass(data['headline'], data['publication'], data['byline']['name'])
    result = get_paragraph(data['paragraphs'])
    art.sub_head = result[0]
    art.body_text = result[1]
    if 'email' in data['byline']:
        art.author_mail = data['byline']['email']
    art.published_at = data['published_at']
    art.publisher = data['publisher']
    art.total_words = get_token_count(art)
    art.path = os.path.basename(file_path)
    return art

def get_paragraph(data):
    sub_heads = []
    body_texts = []
    text = ''
    for d in data:
        if d['kind'] == 'paragraph':
            text += d['value'] + ' '
        elif d['kind'] == 'subheader':
            if text != '':
                body_texts.append(text)
                text = ''
            sub_heads.append(d['value'] + ' ')
    body_texts.append(text)
    return sub_heads, body_texts

def get_token_count(article):
    num_of_words = 0
    all_text = article.headline + ' '
    for text in article.body_text:
        all_text += text
    all_text += ' '
    for text in article.sub_head:
        all_text += text
    num_of_words += len(re.findall(get_token_re_pattern(), all_text.lower()))
    return num_of_words

def get_token_re_pattern():
    return re.compile(r'[0-9]+,[0-9]+|[a-z0-9æøå]{2,}|[0-9]+')

def get_articles_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['content']['articles']
