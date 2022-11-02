import re
from collections import Counter
import spacy
from article.token_class import TokenClass
NLP = spacy.load('da_core_news_sm')

def add_tokens_to_articles(articles):
    for art in articles:
        all_body = ''
        all_sub_head = ''
        for body in art.body_text:
            all_body += body
        for sub_head in art.sub_head:
            all_sub_head += sub_head
        tokens = make_tokens(all_body, 3) # order is important
        tokens.extend(make_tokens(all_sub_head, 2)) # order is important
        tokens.extend(make_tokens(art.headline, 1)) # order is important
        tokens = remove_duplicates(tokens)
        art.tokens = tokens
        break
    return articles

def remove_duplicates(tokens):
    trimmed_tokens = my_dictionary()
    tokens.sort(key=lambda x: x.rank)
    for t in tokens:
        if t.word not in trimmed_tokens:
            trimmed_tokens.add(t.word, t.amount, t.rank)
        elif trimmed_tokens[t.word] in trimmed_tokens:
            print('lll')
            trimmed_tokens[t.word][0] += 10

    for k in trimmed_tokens: print(k + ', ' + str(trimmed_tokens[k]))
    return tokens

class my_dictionary(dict):
    # __init__ function
    def __init__(self): 
        self = dict()
          
    # Function to add key:value 
    def add(self, word, amount, rank): 
        self[word] = (amount, rank)

def make_tokens(text, rank):
    token_list = []
    counts = Counter(get_trimmed_words(get_tokens(text)))
    for token in counts:
        token_list.append(TokenClass(token, counts[token], rank))
    return token_list

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
    accepted_chars_pattern = re.compile(r'[0-9]+,[0-9]+|[a-z0-9æøå]{2,}|[0-9]+')
    words = []
    for match in accepted_chars_pattern.finditer(text):
        words.append(match.group())
    return words
