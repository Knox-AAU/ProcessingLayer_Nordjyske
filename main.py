from datetime import datetime
import os
import sys
from article.json_parser import get_parsed_articles
from vec_words.extract_words import add_tokens_to_articles
from data_api.insert import insert_articles_tokens
from console import print_error, update_status_console, console_confirmation
from exceptions import HttpException

TEST_DATA_PATH = 'jsonTestData/'

def process_insert_articles(path, current_file, start_time):
    update_status_console(len(os.listdir(TEST_DATA_PATH)), current_file, start_time)
    articles = get_parsed_articles(path)
    articles = add_tokens_to_articles(articles)
    insert_articles_tokens(articles)

def main():
    console_confirmation()
    start_time = datetime.now()
    files = os.listdir(TEST_DATA_PATH)
    try:
        for (root, dirs, files) in os.walk(TEST_DATA_PATH):
            for index, file in enumerate(files):
                process_insert_articles(os.path.join(TEST_DATA_PATH, file), index, start_time)
    except HttpException as e:
        print_error('HttpException: ' + str(e))
main()
