from collections import Counter
import spacy
from vec_words.token_dict_class import TokenDict
from article.json_parser import get_token_re_pattern
NLP = spacy.load('da_core_news_sm')

def add_tokens_to_articles(articles):
    for art in articles:
        all_body = ''
        all_sub_head = ''
        for body in art.body_text:
            all_body += body
        for sub_head in art.sub_head:
            all_sub_head += sub_head
        tokens = make_tokens(art.headline, 1) # order is important
        tokens.extend(make_tokens(all_sub_head, 2)) # order is important
        tokens.extend(make_tokens(all_body, 3)) # order is important
        art.tokens = tokens
    return articles

def make_tokens(text, rank):
    tokens_dict = TokenDict()
    tokens = get_tokens(text)
    if len(tokens) == 0:
        return TokenDict()
    counts = Counter(get_trimmed_words(tokens))
    for token in counts:
        tokens_dict.add(token, counts[token], rank)
    return tokens_dict

def get_trimmed_words(words):
    words_str = ' '.join(words)
    doc = NLP(words_str)
    word_lemmas = []
    for token in doc:
        if not token.is_stop:
            word_lemmas.append(token.lemma_)
    return word_lemmas

def get_tokens(text):
    text = text.lower()
    accepted_tokens_pattern = get_token_re_pattern()
    words = []
    for match in accepted_tokens_pattern.finditer(text):
        words.append(match.group())
    return words
