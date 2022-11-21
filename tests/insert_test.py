import unittest
from article.article_class import ArticleClass
from data_handler.insert import get_content_json
from data_handler.insert import get_tokens_json


class TestInsertArticlesTokens(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
