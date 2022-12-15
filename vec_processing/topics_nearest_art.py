from datetime import datetime
from data_handler.fetch import fetch_editable_categories
from data_handler.update import update_document_category
from data_handler.insert import insert_category_amount, insert_nearest_arts
from data_handler.delete import delete_categories, delete_nearest_arts
from data_handler.file_load_save import save_json_data, load_json_data
from vec_processing.find_topics import find_topics
from vec_processing.find_nearest_articles import get_nearest_arts
from console import print_warning, confirmation_insert_new_categories, print_process_percent

NEAREAST_ARTS_AMOUNT = 5
TOPICS_FILE_NAME = 'topics.json'
NEAREAST_ARTS_FILE_NAME = 'neareast_docs.json'
PRINTOUT_DIVIDER = 1000

def store_topics_nearest_docs(word_vecs, storage_path):
    start_time = datetime.now()
    print('Start clustering...')
    vecs, ids = split_2d_list(word_vecs)
    topics = find_topics(vecs, ids)
    print('Saving topics...')
    save_json_data(storage_path, TOPICS_FILE_NAME, topics)
    print(f'Topics made and saved in: {datetime.now() - start_time}')
    print('Finding nearest articles...')
    neareast_arts = get_nearest_arts(vecs, ids, NEAREAST_ARTS_AMOUNT)
    print('Saving neareast docs...')
    save_json_data(storage_path, NEAREAST_ARTS_FILE_NAME, neareast_arts)
    print(f'Total time: {datetime.now() - start_time}')

def set_topics(api_url, storage_path):
    topics_data = load_json_data(storage_path+TOPICS_FILE_NAME)
    n_clusters = topics_data['n_clusters']
    topics = topics_data['topics']
    db_ids = fetch_editable_categories(api_url)
    if len(db_ids) != n_clusters:
        print_warning('Categories in database does not have to same length as the stored topics')
        if confirmation_insert_new_categories():
            delete_categories(api_url, db_ids)
            insert_category_amount(api_url, n_clusters)
        else:
            return
    set_documents_topics(api_url, topics)

def set_documents_topics(api_url, topics):
    text = 'Updating category on documents in db...'
    print(text)
    db_ids = fetch_editable_categories(api_url)
    start_time = datetime.now()
    for index, category in enumerate(topic_to_category(topics, db_ids)):
        if index % (len(topics)/PRINTOUT_DIVIDER) == 0: # for a slow printout
            print_process_percent(text, index+1 , len(topics), start_time)
        update_document_category(api_url, category)
    print(f'Category on {len(topics)} documents updated')

def topic_to_category(topics, db_ids):
    categories = []
    for topic in topics:
        categories.append({'id': topic['id'], 'category': db_ids[topic['topic']]})
    return categories

def split_2d_list(word_vecs):
    vecs = []
    ids = []
    for word_vec in word_vecs:
        vecs.append(word_vec['vec'])
        ids.append(word_vec['id'])
    return vecs, ids

def set_nearest_arts(api_url, storage_path):
    start_time = datetime.now()
    text = 'Updating similar-documents in db...'
    print(text)
    nearest_arts_data = load_json_data(storage_path+NEAREAST_ARTS_FILE_NAME)
    delete_nearest_arts(api_url)
    for index, arts in enumerate(nearest_arts_data):
        insert_nearest_arts(arts, api_url)
        if index % (len(nearest_arts_data)/PRINTOUT_DIVIDER) == 0: # for a slow printout
            print_process_percent(text, index+1 , len(nearest_arts_data), start_time)
