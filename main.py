from tokens.gen_vec_words import store_word_vecs_template
from tokens.words_vecs import get_word_vecs
from articles.articles_handler import insert_arts_db
from data_handler.insert import insert_category_amount
from data_handler.update import update_document_category
from console import print_menu
from vec_processing.kmeans_clustering import find_topics

DATA_PATH = 'jsonTestData/'
STORAGE_PATH = 'storage_data/'
API_URL = 'http://localhost:5501/document-data-api/'

def main():
    match print_menu():
        case '1':
            insert_arts_db(DATA_PATH, API_URL)
        case '2':
            store_word_vecs_template(API_URL, STORAGE_PATH)
        case '3':
            word_vecs = get_word_vecs(API_URL, STORAGE_PATH)
            topics = find_topics(word_vecs)
            insert_category_amount(API_URL)
            update_document_category(API_URL, topics)
        case _:
            print('Input was not correct')
main()
