import unittest
from articles import article_class
from tokens.gen_vec_words import get_only_words
from tokens.gen_vec_words import get_words_from_articles

class TestMakeUniqueWords(unittest.TestCase):
    def test_get_only_words_params(self):
        param_list = [('foo o', ['foo']), ('', []), ('f o o o', []), ('f....o.o', []),
                      ('f-o', []), ('foo-oo', ['foo', 'oo']), ('FOO', ['foo']),
                      ('   ', []), ('32432', []), ('cat234', ['cat'])]
        for p_1, p_2 in param_list:
            with self.subTest():
                self.assertEqual(get_only_words(p_1), p_2)


class TestGetUniqueWords(unittest.TestCase):
    def test_get_words_from_articles(self):
        art = article_class.ArticleClass(
            headline='headline', publication='publication', author_name='name')
        param_list = [
            ('hunden er sød',{'hund': 1}),
            ('hund er sød og hunden hedder poison',{'hund': 2, 'poison': 1}),
            ('hund er sej og hunden hedder peter',{'hund': 2}),
            ('Det er godt Nok bare 0 fedt AT have dyr!!!!',{}),
            ('Jeg har spist skildpadde i dag',{'dag': 1}),
        ]
        for p_1, p_2 in param_list:
            with self.subTest():
                art.body_text = p_1
                self.assertEqual(get_words_from_articles([art]), p_2)

if __name__ == '__main__':
    unittest.main()
