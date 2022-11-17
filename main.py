from datetime import datetime
import os
from articles.json_parser import get_parsed_articles
from tokens.extract_tokens import add_tokens_to_articles
from data_api.insert import insert_articles_tokens
from data_api.update import update_word_relevance
from console import print_error, update_status_console, console_confirmation, print_success
from exceptions import HttpException

DATA_PATH = 'jsonTestData/'
API_URL = 'http://localhost:5501/document-data-api/'

def get_articles_tokens(files, start_time):
    for file in files:
        update_status_console(len(os.listdir(DATA_PATH)), file['index'], start_time)
        articles = get_parsed_articles(file['path'])
        articles = add_tokens_to_articles(articles)
    return articles   

def get_files_data(path):
    all_files = []
    files = os.listdir(path)
    for (root, dirs, files) in os.walk(path):
            for index, file in enumerate(files):
                all_files.append({'path': os.path.join(DATA_PATH, file), 'index': index})
    return all_files

def main():
    console_confirmation()
    start_time = datetime.now()
    try:
        files = get_files_data(DATA_PATH)
        articles = get_articles_tokens(files, start_time)
        #insert_articles_tokens(articles, API_URL)
        print_success(start_time, len(files))
        #update_word_relevance(API_URL)
    except HttpException as e:
        print_error('HttpException: ' + str(e))
main()
