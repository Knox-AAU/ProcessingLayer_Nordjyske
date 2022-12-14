import re
import os
from articles.article_class import ArticleClass
from articles.validation import is_valid
from data_handler.file_load_save import load_json_data

def get_parsed_articles(file_path):
    data_objs = load_json_data(file_path)['content']['articles']
    parsed_articles = []
    for data_obj in data_objs:
        if is_valid(data_obj):
            parsed_articles.append(parse_article(data_obj, file_path))
    return parsed_articles

def remove_duplicates(articles):
    return list({item.data_id:item for item in articles}.values())

def parse_article(data, file_path):
    art = ArticleClass(data['headline'], data['publication'], data['byline']['name'])
    sub, body = get_paragraph(data['paragraphs'])
    art.sub_head = sub
    art.body_text = body
    art.published_at = data['published_at']
    art.publisher = data['publisher']
    art.data_id = data['id']
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
    num_of_tokens = 0
    all_text = article.headline + ' '
    for text in article.body_text:
        all_text += text
    all_text += ' '
    for text in article.sub_head:
        all_text += text
    num_of_tokens += len(re.findall(get_token_re_pattern(), all_text.lower()))
    return num_of_tokens

def get_token_re_pattern():
    return re.compile(r'[0-9]+,[0-9]+|[a-z0-9æøå]{2,}|[0-9]+')
