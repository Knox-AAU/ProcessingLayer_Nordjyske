from article.json_parser import get_parsed_articles

JSON_FILE_PATH = 'jsonTestData/2017-06-08_himmerland.json'

def main():
    articles = get_parsed_articles(JSON_FILE_PATH)
    print(len(articles))

main()
