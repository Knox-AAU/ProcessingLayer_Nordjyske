import unittest
from collections import Counter
from tokens.gen_vec_words import remove_irrelevant, remove_non_words

class WordsVecsTest(unittest.TestCase):
    def test_remove_irrelevant_over_2(self):
        param_list = [('tow tow one', {'one': 1, 'tow': 2}),
                      ('three three three one', {'one': 1}),
                      ('1 2 2 3 3 3', {'1': 1, '2': 2})
                    ]
        for text, expected in param_list:
            with self.subTest():
                words_count = Counter(text.split())
                self.assertEqual(remove_irrelevant(words_count, 2), expected)

    def test_remove_non_words(self):
        param_list = [(['word', 'this', 'ø', 'så'], ['word', 'this', 'ø', 'så']),
                      (['word5'], []),
                      (['word5.78', 'ø8.8', 'word'], ['word']),
                      (['.58', '5', '0.5'], [])
                    ]
        for text, expected in param_list:
            with self.subTest():
                self.assertEqual(remove_non_words(text), expected)

if __name__ == '__main__':
    unittest.main()
