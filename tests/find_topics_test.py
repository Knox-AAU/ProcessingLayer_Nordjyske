import unittest
from vec_processing.find_topics import split_2d_list

class FindTopicsTest (unittest.TestCase):
    def test_split_2d_list(self):
        word_vecs = [{'id': 1, 'vec': [1, 2, 3]},
                     {'id': 2, 'vec': [1, 2, 3]},
                     {'id': 33, 'vec': [11111]},
                     {'id': (), 'vec': []},
                     {'id': (), 'vec': [9, 8, 7]},
                     {'id': (4), 'vec': []}]

        expected_results = (
            [[1, 2, 3], [1, 2, 3], [11111], [], [9, 8, 7], []],
            [1, 2, 33, (), (), 4])
        self.assertEqual(split_2d_list(word_vecs), expected_results)

if __name__ == '__main__':
    unittest.main()
