import unittest
from articles.article_class import ArticleClass
from tokens.token_dict_class import TokenDict
from data_handler.insert import get_content_json
from data_handler.insert import get_tokens_json


class TestInsertArticles(unittest.TestCase):
    def test_get_content_json(self):
        art = ArticleClass('headline', 'publication', 'name')
        art.id = 1
        art.body_text = ['This is body text.']
        expected_output = [{
            'documentId': 1,
            'index': 0,
            'content': 'This is body text.'
        }]
        self.assertEqual(get_content_json(art), expected_output)

class TestInsertTokens(unittest.TestCase):
    def test_get_tokens_json_body_text(self):
        art = ArticleClass('headline', 'publication', 'name')
        art.id = 1
        tokens_dict = TokenDict()
        tokens_dict.add('test1', 1, 3)
        tokens_dict.add('test2', 2, 3)
        tokens_dict.add('test3', 1, 3)
        art.tokens = tokens_dict
        expected_output = [{
            'documentId': 1,
            'word': 'test1',
            'amount': 1,
            'percent': 0.25,
            'rank': 3,
            'clusteringScore': 1
        },
        {
            'documentId': 1,
            'word': 'test2',
            'amount': 2,
            'percent': 0.5,
            'rank': 3,
            'clusteringScore': 2
        },
        {
            'documentId': 1,
            'word': 'test3',
            'amount': 1,
            'percent': 0.25,
            'rank': 3,
            'clusteringScore': 1
        }]
        self.assertEqual(get_tokens_json(art), expected_output)

    def test_get_tokens_json_all(self):
        art = ArticleClass('headline', 'publication', 'name')
        art.id = 1
        tokens_dict = TokenDict()
        tokens_dict.add('test1', 2, 1)
        tokens_dict.add('test2', 2, 2)
        tokens_dict.add('test3', 6, 3)
        art.tokens = tokens_dict
        expected_output = [{
            'documentId': 1,
            'word': 'test1',
            'amount': 2,
            'percent': 0.2,
            'rank': 1,
            'clusteringScore': 3
        },
        {
            'documentId': 1,
            'word': 'test2',
            'amount': 2,
            'percent': 0.2,
            'rank': 2,
            'clusteringScore': 2.5
        },
        {
            'documentId': 1,
            'word': 'test3',
            'amount': 6,
            'percent': 0.6,
            'rank': 3,
            'clusteringScore': 6
        }]
        self.assertEqual(get_tokens_json(art), expected_output)


if __name__ == '__main__':
    unittest.main()
