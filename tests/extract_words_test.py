import unittest
from article.article_class import ArticleClass
from article.token_class import TokenClass
from vec_words.extract_words import add_tokens_to_articles

class TestAddTokensToArticles(unittest.TestCase):
    def test_add_tokens_to_articles(self):
        art_input = ArticleClass(
            headline='headline', publication='publication', author_name='name')
        art_input.body_text = ['test word.']
        art_input.sub_head = ['test test subhead.']

        art_expected = art_input
        art_expected.tokens = [TokenClass('test', 2, 2),
                                TokenClass('word', 1, 3),
                                TokenClass('headline', 1, 1),
                                TokenClass('subhead', 1, 2)]
        self.assertEqual(add_tokens_to_articles([art_input]), art_expected)

if __name__ == '__main__':
    unittest.main()
