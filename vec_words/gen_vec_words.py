import re
import spacy
NLP = spacy.load("da_core_news_sm")

def make_unique_words(text):
    text = text.lower()
    accepted_chars_pattern = re.compile(r"[a-zæøå]{2,}")
    words = []
    for match in accepted_chars_pattern.finditer(text):
        words.append(match.group())
    return words

def get_unique_words(articles):
    unique_words = set()
    for art in articles:
        all_body = ""
        for body in art.body_text:
            all_body += body
        unique_words = unique_words.union(make_unique_words(all_body))
    unique_words = get_lemma_words(unique_words)
    return unique_words

def get_lemma_words(words):
    words_str = ' '.join(words)
    doc = NLP(words_str)
    word_lemmas = set()
    for token in doc:
        if not token.is_stop and token.ent_type_ != "PER":
            word_lemmas.add(token.lemma_)
    return set(word_lemmas)
