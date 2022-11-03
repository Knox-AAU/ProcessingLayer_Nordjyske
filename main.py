from datetime import datetime
import os
from article.json_parser import get_parsed_articles
from vec_words.extract_words import add_tokens_to_articles
from data_api.insert import insert_articles_tokens
from console import *
from exceptions import HttpException

TEST_DATA_PATH = 'jsonTestData/'

def get_articles_in_dir(path):
    files = os.listdir(path)
    articles = []
    for (root, dirs, files) in os.walk(path):
        for file in files:
            articles = (get_parsed_articles(os.path.join(path,file)))
    return articles

def main():
    print('start')
    start_time = datetime.now()
    articles = get_articles_in_dir(TEST_DATA_PATH)
    articles = add_tokens_to_articles(articles)
    try:
        insert_articles_tokens(articles)
    except HttpException as e:
        print_error('HttpException: ' + str(e))

    print('Time to get tokens: '+ str(datetime.now() - start_time))

main()
