import re

def make_unique_words(text):
    text = text.lower()
    accepted_chars_pattern = re.compile(r"[a-zæøå]{2,}")
    words = set()
    for match in accepted_chars_pattern.finditer(text):
        words.add(match.group())
    return words

def get_unique_words(articles, lang_model):
    unique_words = set()
    for art in articles:
        all_body = ""
        for body in art.body_text:
            all_body += body
        unique_words = unique_words.union(make_unique_words(all_body))
    unique_words = get_lemma_words(unique_words, lang_model)
    return unique_words

def get_lemma_words(words, lang_model):
    words_str = ' '.join(words)
    doc = lang_model(words_str)
    word_lemmas = set()
    for token in doc:
        if not token.is_stop and token.ent_type_ != "PER":
            word_lemmas.add(token.lemma_)
    return word_lemmas
