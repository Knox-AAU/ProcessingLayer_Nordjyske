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
    art = ArticleClass(data['headline'], data['publication'], data['byline']['name'])
    result = get_paragraph(data['paragraphs'])
    art.sub_head = result[0]
    art.body_text = result[1]
    if 'email' in data['byline']:
        art.author_mail = data['byline']['email']
    art.published_at = data['published_at']
    art.publisher = data['publisher']
    art.total_words = get_word_count(art)
    return art

def get_paragraph(data):
    sub_heads = []
    body_texts = []
    text = ''
    for d in data:
        if d['kind'] == 'paragraph':
            text += d['value']
        elif d['kind'] == 'subheader':
            if text != '':
                body_texts.append(text)
                text = ''
            sub_heads.append(d['value'])
    body_texts.append(text)
    return sub_heads, body_texts

def get_word_count(art):
    words = []
    for a in art.body_text:
        words.extend(a.split()) #delimiters are assumed to be white space characters
    print(words)
    return len(words)

def get_articles_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['content']['articles']
