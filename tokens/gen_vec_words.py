import re
from datetime import datetime
from collections import Counter
from data_handler.fetch import fetch_tokens
from data_handler.file_load_save import save_json_data
from console import print_process_percent

INCLUDE_TOP_TOKENS = 10000000
SPLIT_LEN = 10000
REMOVE_COUNT_OVER = 350
SELECT_TOP = 1000
VECS_TEMPLATE_FILE_NAME = 'word_vecs_template.json'

def store_word_vecs_template(api_url, storage_path):
    words_count = get_all_words_count(api_url)
    print(f'Done getting vecs template. Highest word count:{words_count.most_common(1)[0]}')
    words = remove_irrelevant(words_count)
    words = [v for v, c in words.most_common(SELECT_TOP)]
    print('Saving word vecs template...')
    save_json_data(storage_path, VECS_TEMPLATE_FILE_NAME, words)

def get_all_words_count(api_url):
    text = 'Getting tokens...'
    print(text)
    start_time = datetime.now()
    words_count = Counter()
    for i in range(int(INCLUDE_TOP_TOKENS/SPLIT_LEN)):
        words_count |= Counter(remove_non_words(fetch_tokens(api_url, SPLIT_LEN, SPLIT_LEN*i)))
        count_text = f'\nCurrent word count: {len(words_count)}'
        print_process_percent(text+count_text, i+1, INCLUDE_TOP_TOKENS/SPLIT_LEN, start_time)
    return words_count

def remove_non_words(tokens_list):
    words = []
    for token in tokens_list:
        if re.match(r'^[a-zæøå]+$', token):
            words.append(token)
    return words

def remove_irrelevant(words_count):
    return Counter({k: c for k, c in words_count.items()if c <= REMOVE_COUNT_OVER})
