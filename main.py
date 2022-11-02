from datetime import datetime
import os
from article.json_parser import get_parsed_articles
from vec_words.extract_words import add_tokens_to_articles
from article.article_class import ArticleClass

TEST_DATA_PATH = '../jsonTestData/'
NUM_OF_FILES_TO_RUN = 1

def get_articles_in_dir(path):
    files = os.listdir(path)
    articles = []
    i = 0
    for (root, dirs, files) in os.walk(path):
        for file in files:
            i = i+1
            articles = (get_parsed_articles(os.path.join(path,file)))           
            if i == NUM_OF_FILES_TO_RUN:
                break
    return articles

def main():
    print('start')

    art_input = ArticleClass(
        headline='head line word', publication='publication', author_name='name')
    art_input.body_text = ['test test. word']
    art_input.sub_head = ['test test word.']

    k = add_tokens_to_articles([art_input])
    print(k)
"""
    start_time = datetime.now()
    articles = get_articles_in_dir(TEST_DATA_PATH)
    articles = add_tokens_to_articles(articles)
    #for t in articles[0].tokens: print(t.word + ', ' + str(t.amount) + ', ' + str(t.rank))
    print('Time to get tokens: '+ str(datetime.now() - start_time))
"""
main()
