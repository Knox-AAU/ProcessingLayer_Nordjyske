from tokens.gen_vec_words import store_word_vecs_template
from tokens.words_vecs import get_word_vecs
from articles.articles_handler import insert_arts_db
from console import print_menu
from vec_processing.processing_handler import store_clusters_nearest_arts, set_clusters, set_nearest_arts

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
            store_clusters_nearest_arts(word_vecs, STORAGE_PATH)
        case '4':
            set_clusters(API_URL, STORAGE_PATH)
            set_nearest_arts(API_URL, STORAGE_PATH)
        case _:
            print('Input was not correct')
main()
