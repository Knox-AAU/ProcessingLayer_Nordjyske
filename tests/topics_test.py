import unittest
from vec_processing.topics_nearest_art import update_topics
from vec_processing.topics_nearest_art import split_2d_list

class TopicsTest(unittest.TestCase):
    def test_update_topics(self):
        topics = [
            {'id': 1, 'topic': 0},
            {'id': 1, 'topic': 1},
            {'id': 1, 'topic': 2},
            {'id': 1, 'topic': 1},
            {'id': 1, 'topic': 3}
        ]
        db_ids = [1, 5, 77, 2]
        self.assertEqual(update_topics(topics, db_ids), [
            {'id': 1, 'category': 1},
            {'id': 1, 'category': 5},
            {'id': 1, 'category': 77},
            {'id': 1, 'category': 5},
            {'id': 1, 'category': 2}
        ])

    def test_update_topics_no_match(self):
        topics = [{'id': 1, 'topic': 4}]
        db_ids = [1, 2, 3]
        with self.assertRaises(IndexError):
            update_topics(topics, db_ids)

class TopicsNearestDocTest(unittest.TestCase):
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
