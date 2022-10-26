import unittest
import spacy
from article import article_class
from vec_words.gen_vec_words import make_unique_words
from vec_words.gen_vec_words import get_unique_words
NLP = spacy.load("da_core_news_sm")


class TestMakeUniqueWords(unittest.TestCase):
    def test_make_unique_words_params(self):
        param_list = [('foo o', {'foo'}), ('', set()), ('f o o o', set()), ('f....o.o', set()),
                      ('f-o o', set()), ('foo-oo', {'foo', 'oo'}), ('FOO', {'foo'}), ('   ', set())]
        for p_1, p_2 in param_list:
            with self.subTest():
                self.assertEqual(make_unique_words(p_1), p_2)


class TestGetUniqueWords(unittest.TestCase):
    def test_get_unique_words_params(self):
        art = article_class.ArticleClass(
            headline=['headline'], publication=['publication'], author_name=['name'])
        param_list = [
            ('hunden er sød', {'sød', 'hund'}), ('hun-den er sød', {'sød'}),
            ('hu3n er sej', {'hu', 'sej'}), ('HAN KODER MEGET', {'kode'})]
        for p_1, p_2 in param_list:
            art_array = []
            art.body_text = p_1
            art_array.append(art)
            with self.subTest():
                self.assertEqual(get_unique_words(
                    art_array, NLP), p_2)


if __name__ == '__main__':
    unittest.main()
