from datetime import datetime
from data_handler.fetch import fetch_changeable_categories, fetch_article_count, fetch_documents
from data_handler.update import update_document_category, update_categorys_to_default
from data_handler.insert import insert_category_amount
from data_handler.delete import delete_categorys
from data_handler.file_load_save import save_json_data, load_json_data
from vec_processing.find_topics import find_topics
from vec_processing.find_nearest_articles import get_neareast_arts
from console import print_warning, confirmation_insert_new_categories
from exceptions import HttpException

NEAREAST_ARTS_AMOUNT = 5

TOPICS_FILE_NAME = 'topics.json'
NEAREAST_DOCS_FILE_NAME = 'neareast_docs.json'

def store_topics_nearest_docs(word_vecs, storage_path):
    start_time = datetime.now()
    print('Start clustering...')
    topics = find_topics(word_vecs)
    print('Saving topics...')
    save_json_data(storage_path, TOPICS_FILE_NAME, topics)
    print('Topics made and saved in: ' + str(datetime.now() - start_time))
    print('Finding nearest articles...')
    neareast_docs = get_neareast_arts(word_vecs, NEAREAST_ARTS_AMOUNT)
    print('Saving neareast docs...')
    save_json_data(storage_path, NEAREAST_DOCS_FILE_NAME, neareast_docs)
    print('Total time: ' + str(datetime.now() - start_time))

def insert_categorys(api_url, storage_path):
    topics_data = load_json_data(storage_path+TOPICS_FILE_NAME)
    n_clusters = topics_data['n_clusters']
    topics = topics_data['topics']
    db_ids = fetch_changeable_categories(api_url)
    if len(db_ids) != topics:
        print_warning('Categories in database does not have to same length as the stored topics')
        if confirmation_insert_new_categories():
            reset_categorys(api_url, db_ids, n_clusters)
        else:
            return
    update_document_category(api_url, update_topics(topics))

def reset_categorys(api_url, db_ids, n_clusters):
    art_count = fetch_article_count(api_url)
    first_art_id = fetch_documents(api_url, 1, 0)[0]['id']
    try:
        update_categorys_to_default(api_url, art_count, first_art_id)
    except HttpException as e:
        print_warning(f'Article skipped: {e}')
    delete_categorys(api_url, db_ids)
    insert_category_amount(api_url, n_clusters)

def update_topics(topics, db_ids):
    new_topics = []
    for topic in topics:
        new_topics.append({'id': topic['id'], 'category': db_ids[topic['topic']]})
    return new_topics

def insert_nearest_docs(api_url, storage_path):
    print('not implemented')
