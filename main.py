from datetime import datetime
import os
import spacy
from article.json_parser import get_parsed_articles
from vec_words.gen_vec_words import get_unique_words
NLP = spacy.load("da_core_news_sm")

TEST_DATA_PATH = 'jsonTestData/'

def get_articles_in_dir(path):
    articles = []
    files = os.listdir(path)
    for (root, dirs, files) in os.walk(path):
        for file in files:
            articles.extend(get_parsed_articles(os.path.join(path,file)))
    return articles

def main():
    print("start")
    startTime = datetime.now()
    articles = get_articles_in_dir(TEST_DATA_PATH)
    print("parser time: "+ str(datetime.now() - startTime))
    startTime = datetime.now()
    print('Num of articles: ' + str(len(articles)))
    words = get_unique_words(articles, NLP)
    print("gen_vec_words time: "+ str(datetime.now() - startTime))
    print('Num of unique words: ' + str(len(words)))
main()
