import re
from collections import Counter
from data_handler.fetch import fetch_tokens

TOKENS_LEN = 10000
SPLIT_LEN = 1000
REMOVE_COUNT_UNDER = 5

def get_words_count(api_url):
    words_count = get_all_words_count(api_url)
    words = remove_irrelevant(words_count)
    print('Done total word count: ' + str(len(words)))
    return words

def get_all_words_count(api_url):
    print('Getting tokens:')
    words_count = Counter()
    for i in range(int(TOKENS_LEN/SPLIT_LEN)):
        words_count |= Counter(remove_non_words(fetch_tokens(api_url, SPLIT_LEN, SPLIT_LEN*i)))
        print('Index: ' + str(i) + ', words len: ' + str(len(words_count)))
    return words_count

def remove_non_words(tokens_list):
    words = []
    for token in tokens_list:
        if re.match(r'^[a-zæøå]+$', token):
            words.append(token)
    return words

def remove_irrelevant(words_count):
    return Counter({k: c for k, c in words_count.items() if c >= REMOVE_COUNT_UNDER})
