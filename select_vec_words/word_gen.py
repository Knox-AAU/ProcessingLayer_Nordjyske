from article.json_parser import get_parsed_articles

def do_thing():
    articles = get_parsed_articles('../jsonTestData/2017-06-08_himmerland.json')
    for art in articles:
        bodys = ""
        for body in art.body_text:
            bodys += body
        print(dict.fromkeys(bodys.split()))


