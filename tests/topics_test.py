import unittest
from vec_processing.topics_nearest_art import update_topics

class TestTopicsNearestDoc(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
