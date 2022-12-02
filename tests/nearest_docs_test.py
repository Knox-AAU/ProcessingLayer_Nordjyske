import unittest
import math
from vec_processing.find_nearest_articles import get_nearest_arts

class TestGetNearestDocument (unittest.TestCase):
    def test_get_nearest_document_2d(self):
        article_vector_list = [
            {'id': 1, 'vec': [1, 2, 3]},
            {'id': 2, 'vec': [10, 9, 8]}
        ]
        expected_output = [
            {'art_id': 1, 'nearest': [
                {'id': 2, 'dist': math.sqrt(((10-1)**2)+((9-2)**2)+((8-3)**2))}
            ]},
            {'art_id': 2, 'nearest': [
                {'id': 1, 'dist': math.sqrt(((1-10)**2)+((2-9)**2)+((3-8)**2))}
            ]}
        ]
        self.assertEqual(get_nearest_arts(article_vector_list, 1), expected_output)

    def test_get_nearest_document_2d_zero(self):
        article_vector_list = [
            {'id': 1, 'vec': [0.33, 0.33, 0.33]},
            {'id': 2, 'vec': [0.33, 0.33, 0.33]}
        ]
        expected_output = [{'art_id': 1, 'nearest': [
            {'id': 1, 'dist': 0.0}
        ]},
        {'art_id': 2, 'nearest': [
            {'id': 1, 'dist': 0.0}
        ]}]
        self.assertEqual(get_nearest_arts(article_vector_list, 1), expected_output)

    def test_get_nearest_document_2d_normalize(self):
        article_vector_list = [
            {'id': 1, 'vec': [0.2672, 0.5345, 0.8017]},
            {'id': 2, 'vec': [0.5659, 0.1616, 0.8084]}
        ]
        expected_output = [
            {'art_id': 1, 'nearest':
                [{'id': 2, 'dist': math.sqrt(((0.5659-0.2672)**2)+((0.1616-0.5345)**2)+((0.8084-0.8017)**2))}]},
            {'art_id': 2, 'nearest':
                [{'id': 1, 'dist': math.sqrt(((0.2672-0.5659)**2)+((0.5345-0.1616)**2)+((0.8017-0.8084)**2))}]}
        ]

        self.assertEqual(get_nearest_arts(article_vector_list, 1), expected_output)

    def test_get_nearest_document_3d(self):
        article_vector_list = [
            {'id': 1, 'vec': [1, 2, 3]},
            {'id': 4, 'vec': [10, 9, 8]},
            {'id': 2, 'vec': [5, 1, 4]}
        ]
        expected_output = [
            {'art_id': 1, 'nearest': [{'id': 2, 'dist': math.sqrt(((5-1)**2)+((1-2)**2)+((4-3)**2))},
                {'id': 4, 'dist': math.sqrt(((10-1)**2)+((9-2)**2)+((8-3)**2))}]},
            {'art_id': 4, 'nearest': [{'id': 2, 'dist': math.sqrt(((5-10)**2)+((1-9)**2)+((4-8)**2))},
                {'id': 1, 'dist': math.sqrt(((1-10)**2)+((2-9)**2)+((3-8)**2))}]},
            {'art_id': 2, 'nearest': [{'id': 1, 'dist': math.sqrt(((1-5)**2)+((2-1)**2)+((3-4)**2))},
                {'id': 4, 'dist': math.sqrt(((10-5)**2)+((9-1)**2)+((8-4)**2))}]}
        ]
        self.assertEqual(get_nearest_arts(article_vector_list, 2), expected_output)

if __name__ == '__main__':
    unittest.main()
