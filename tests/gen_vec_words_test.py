from re import S
import unittest
from article import article_class
from vec_words.gen_vec_words import make_unique_words
from vec_words.gen_vec_words import get_unique_words


class TestMakeUniqueWords(unittest.TestCase):
    def test_make_unique_words_params(self):
        param_list = [('foo o', ['foo']), ('', []), ('f o o o', []), ('f....o.o', []),
                      ('f-o o', []), ('foo-oo', ['foo', 'oo']), ('FOO', ['foo']), ('   ', [])]
        for p_1, p_2 in param_list:
            with self.subTest():
                self.assertEqual(make_unique_words(p_1), p_2)


class TestGetUniqueWords(unittest.TestCase):
    def test_get_unique_words(self):
        art = article_class.ArticleClass(
            headline=['headline'], publication=['publication'], author_name=['name'])
        art.body_text = 'hunden er sød'
        art_array = []
        art_array.append(art)
        result_set = {'sød', 'hund'}
        self.assertEqual(get_unique_words(art_array), result_set)


if __name__ == '__main__':
    unittest.main()
