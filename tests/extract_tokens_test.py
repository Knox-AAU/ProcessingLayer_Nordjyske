import unittest
from article.article_class import ArticleClass
from vec_words.extract_tokens import add_tokens_to_articles
from vec_words.token_dict_class import TokenDict

class TestAddTokensToArticles(unittest.TestCase):
    def test_add_tokens_to_articles_general(self):
        art_input = ArticleClass('headline', 'publication', 'name')
        art_input.sub_head = ['test test subhead.']
        art_input.body_text = ['test word.']
        tokens = TokenDict()
        tokens.add('headlin', 1, 1)
        tokens.add('test', 3, 2)
        tokens.add('subhead', 1, 2)
        tokens.add('word', 1, 3)
        art_output = add_tokens_to_articles([art_input])
        self.assertDictEqual(art_output[0].tokens, tokens)

    def test_add_tokens_to_articles_one_for_each(self):
        art_input = ArticleClass('test', 'publication', 'name')
        art_input.sub_head = ['test test test2.']
        art_input.body_text = ['test test2 test1']
        tokens = TokenDict()
        tokens.add('test', 4, 1)
        tokens.add('test1', 1, 3)
        tokens.add('test2', 2, 2)
        art_output = add_tokens_to_articles([art_input])
        self.assertDictEqual(art_output[0].tokens, tokens)


    def test_add_tokens_to_articles_same_count(self):
        art_input = ArticleClass('test1', 'publication', 'name')
        art_input.sub_head = ['test2']
        art_input.body_text = ['test3']
        tokens = TokenDict()
        tokens.add('test1', 1, 1)
        tokens.add('test2', 1, 2)
        tokens.add('test3', 1, 3)
        art_output = add_tokens_to_articles([art_input])
        self.assertDictEqual(art_output[0].tokens, tokens)

    def test_add_tokens_to_articles_no_sub(self):
        art_input = ArticleClass('test1 test2', 'publication', 'name')
        art_input.body_text = ['test2 test2 ']
        tokens = TokenDict()
        tokens.add('test1', 1, 1)
        tokens.add('test2', 3, 1)
        art_output = add_tokens_to_articles([art_input])
        self.assertDictEqual(art_output[0].tokens, tokens)

if __name__ == '__main__':
    unittest.main()
