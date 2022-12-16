import unittest
from vec_processing.processing_handler import cluster_to_category
from vec_processing.processing_handler import split_2d_list

class ClustersTest(unittest.TestCase):
    def test_clusters_to_category(self):
        clusters = [
            {'id': 1, 'cluster': 0},
            {'id': 1, 'cluster': 1},
            {'id': 1, 'cluster': 2},
            {'id': 1, 'cluster': 1},
            {'id': 1, 'cluster': 3}
        ]
        db_ids = [1, 5, 77, 2]
        self.assertEqual(cluster_to_category(clusters, db_ids), [
            {'id': 1, 'category': 1},
            {'id': 1, 'category': 5},
            {'id': 1, 'category': 77},
            {'id': 1, 'category': 5},
            {'id': 1, 'category': 2}
        ])

    def test_cluster_to_category_no_match(self):
        clusters = [{'id': 1, 'cluster': 4}]
        db_ids = [1, 2, 3]
        with self.assertRaises(IndexError):
            cluster_to_category(clusters, db_ids)

class ProcessingHandlerTest(unittest.TestCase):
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
