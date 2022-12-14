from datetime import datetime
from data_handler.file_load_save import load_json_data, save_json_data
from data_handler.fetch import fetch_article_count, fetch_word_vecs
from tokens.gen_vec_words import VECS_TEMPLATE_FILE_NAME
from console import print_warning, confirmation_get_new_vecs, print_process_percent
from exceptions import FileNotExistsException

SPLIT_LEN = 1000
VECS_FILE_NAME = 'word_vecs.json'

def get_vecs_db(api_url, storage_path):
    text = 'Creating word vecs from database...'
    print(text)
    start_time = datetime.now()
    vecs_template = load_json_data(storage_path + VECS_TEMPLATE_FILE_NAME)
    art_count = fetch_article_count(api_url)
    word_vecs = []
    for i in range(int(art_count/SPLIT_LEN)):
        print_process_percent(text, i+1, art_count/SPLIT_LEN, start_time)
        word_vecs.extend(fetch_word_vecs(api_url, SPLIT_LEN, SPLIT_LEN*i, vecs_template))
    print('Saving word vecs...')
    save_json_data(storage_path, VECS_FILE_NAME, word_vecs)
    return word_vecs

def get_vecs_storage(api_url, storage_path):
    try:
        return load_json_data(storage_path + VECS_FILE_NAME)
    except FileNotExistsException:
        print_warning('Word vecs not found')
        return get_vecs_db(api_url, storage_path)

def get_word_vecs(api_url, storage_path):
    print('Getting word vecs from storage...')
    if confirmation_get_new_vecs():
        return get_vecs_db(api_url, storage_path)
    else:
        return get_vecs_storage(api_url, storage_path)
