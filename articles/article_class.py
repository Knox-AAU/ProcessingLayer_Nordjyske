from tokens.token_dict_class import TokenDict

class ArticleClass:
    def __init__(self, headline, publication, author_name):
        self.headline = headline
        self.publication = publication
        self.author_name = author_name
    publisher = ''
    published_at = ''
    data_id = 0
    total_words = 0
    tokens = {}
    sub_head = []
    body_text = []
    path = ''
    tokens = TokenDict()
