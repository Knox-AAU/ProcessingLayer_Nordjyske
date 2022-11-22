import re
from collections import Counter
from data_handler.fetch import fetch_tokens
from data_handler.file_load_save import save_json_data

TOKENS_LEN = 10000
SPLIT_LEN = 1000
REMOVE_COUNT_UNDER = 5
REMOVE_COUNT_OVER = 50
SELECT_TOP = 200
VECS_TEMPLATE_FILE_NAME = 'word_vecs_template.json'

def store_word_vecs_template(api_url, storage_path):
    words_count = get_all_words_count(api_url)
    print('Done getting vecs template. Highest word count: ' + str(words_count.most_common(1)[0]))
    words = remove_irrelevant(words_count)
    words = [v for v, c in words.most_common(SELECT_TOP)]
    save_json_data(storage_path, VECS_TEMPLATE_FILE_NAME, words)

def get_all_words_count(api_url):
    print('Getting tokens:')
    words_count = Counter()
    for i in range(int(TOKENS_LEN/SPLIT_LEN)):
        words_count |= Counter(remove_non_words(fetch_tokens(api_url, SPLIT_LEN, SPLIT_LEN*i)))
        print(str(i+1) + ' of ' + str(int(TOKENS_LEN/SPLIT_LEN)) + ', words len: ' + str(len(words_count)))
    return words_count

def remove_non_words(tokens_list):
    words = []
    for token in tokens_list:
        if re.match(r'^[a-zæøå]+$', token):
            words.append(token)
    return words

def remove_irrelevant(words_count):
    return Counter({k: c for k, c in words_count.items()
        if c >= REMOVE_COUNT_UNDER and c <= REMOVE_COUNT_OVER
        })
