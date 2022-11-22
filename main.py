from data_handler.file_load_save import save_words_count
from tokens.gen_vec_words import get_words_count
from articles.articles_handler import insert_arts_db
from console import print_menu

DATA_PATH = 'jsonTestData/'
STORAGE_PATH = 'storage_data/'
API_URL = 'http://localhost:5501/document-data-api/'

def main():
    match print_menu():
        case '1':
            insert_arts_db(DATA_PATH, API_URL)
        case '2':
            words_count = get_words_count(API_URL)
            save_words_count(STORAGE_PATH, words_count)
        case '3':
            print('Not implemented')
main()
