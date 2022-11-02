import unittest
from article import article_class
from vec_words.gen_vec_words import get_only_words
from vec_words.gen_vec_words import get_words_from_articles

class TestMakeUniqueWords(unittest.TestCase):
    def test_get_only_words_params(self):
        param_list = [('foo o', ['foo']), ('', []), ('f o o o', []), ('f....o.o', []),
                      ('f-o', []), ('foo-oo', ['foo', 'oo']), ('FOO', ['foo']),
                      ('   ', []), ('32432', []), ('cat234', ['cat'])]
        for p_1, p_2 in param_list:
            with self.subTest():
                self.assertEqual(get_only_words(p_1), p_2)


class TestGetUniqueWords(unittest.TestCase):
    def test_get_words_from_articles_1(self):
        art = article_class.ArticleClass(headline='headline', publication='publication', author_name='name')
        param_list = [
            ('hunden er sød',{'hund': 1}),
            ('hund er sød og hunden hedder poison',{'hund': 2, 'poison': 1}),
            ('Det er godt Nok bare 0 fedt AT have dyr!!!!',{}),
            ('Jeg har spist skildpadde i dag',{'skildpadde': 1, 'dag': 1}),
        ]
        for p_1, p_2 in param_list:
            with self.subTest():
                art.body_text = p_1
                self.assertEqual(get_words_from_articles([art]), p_2)

if __name__ == '__main__':
    unittest.main()
