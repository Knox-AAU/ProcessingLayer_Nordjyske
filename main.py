from datetime import datetime
import os
from article.json_parser import get_parsed_articles
from vec_words.extract_tokens import add_tokens_to_articles
from data_api.insert import insert_articles_tokens
from console import print_error, update_status_console, console_confirmation, print_success
from exceptions import HttpException

DATA_PATH = 'jsonTestData/'
API_URL = 'http://localhost:5501/document-data-api/'

def process_insert_articles(path, current_file, start_time):
    update_status_console(len(os.listdir(DATA_PATH)), current_file, start_time)
    articles = get_parsed_articles(path)
    articles = add_tokens_to_articles(articles)
    insert_articles_tokens(articles, API_URL)

def main():
    console_confirmation()
    start_time = datetime.now()
    files = os.listdir(DATA_PATH)
    try:
        for (root, dirs, files) in os.walk(DATA_PATH):
            for index, file in enumerate(files):
                process_insert_articles(os.path.join(DATA_PATH, file), index, start_time)
        print_success(start_time, len(files))
    except HttpException as e:
        print_error('HttpException: ' + str(e))
main()
