import re
import spacy
from collections import Counter
NLP = spacy.load("da_core_news_sm")

def get_only_words(text):
    text = text.lower()
    accepted_chars_pattern = re.compile(r'[a-zæøå]{2,}')
    words = []
    for match in accepted_chars_pattern.finditer(text):
        words.append(match.group())
    return words

def get_words_from_articles(articles):
    words = []
    for art in articles:
        all_body = ''
        for body in art.body_text:
            all_body += body
        words.extend(get_only_words(all_body))
    trimmed_words = get_trimmed_words(words)
    return Counter(trimmed_words)

def get_trimmed_words(words):
    words_str = ' '.join(words)
    doc = NLP(words_str)
    allow_postags = set(['NOUN', 'PROPN'])
    word_lemmas = []
    for token in doc:
        if not token.is_stop and token.ent_type_ != 'PER' and token.pos_ in allow_postags:
            word_lemmas.append(token.lemma_)
    return word_lemmas
