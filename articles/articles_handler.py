import os
from datetime import datetime
from articles.json_parser import get_parsed_articles
from articles.json_parser import remove_duplicates
from tokens.extract_tokens import add_tokens_to_articles
from data_handler.insert import insert_articles_tokens
from data_handler.file_load_save import get_files_data
from data_handler.update import update_word_relevance
from console import print_error, update_status_console, confirmation_insert_arts, print_success
from exceptions import HttpException

def insert_arts_db(data_path, api_url):
    confirmation_insert_arts()
    start_time = datetime.now()
    try:
        files = get_files_data(data_path)
        articles = get_articles_tokens(files, start_time, data_path)
        print('Remove_duplicates...')
        articles = remove_duplicates(articles)
        print('Insert_articles_tokens...')
        insert_articles_tokens(articles, api_url)
        print_success(start_time, len(files))
        update_word_relevance(api_url)
    except HttpException as e:
        print_error('HttpException: ' + str(e))

def get_articles_tokens(files, start_time, data_path):
    articles = []
    for file in files:
        update_status_console(len(os.listdir(data_path)), file['index'], start_time)
        arts = get_parsed_articles(file['path'])
        articles.extend(add_tokens_to_articles(arts))
    return articles
