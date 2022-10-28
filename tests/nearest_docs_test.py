import unittest
import math
from article.find_nearest_document import get_neareast_docs

class TestGetNearestDocument (unittest.TestCase):
    def test_get_nearest_document_2d(self):
        article_vector_list = [
            [1, [1, 2, 3]],
            [2, [10, 9, 8]]
        ]
        expected_output = [
            [1, [[2, math.sqrt(((10-1)**2)+((9-2)**2)+((8-3)**2))]]],
            [2, [[1, math.sqrt(((1-10)**2)+((2-9)**2)+((3-8)**2))]]]
        ]

        self.assertEqual(get_neareast_docs(article_vector_list), expected_output)

    def test_get_nearest_document_2d_zero(self):
        article_vector_list = [
            [1, [0.33, 0.33, 0.33]],
            [2, [0.33, 0.33, 0.33]]
        ]
        expected_output = [[1, []], [2, []]]

        self.assertEqual(get_neareast_docs(article_vector_list), expected_output)

    def test_get_nearest_document_2d_normalize(self):
        article_vector_list = [
            [1, [0.2672, 0.5345, 0.8017]],
            [2, [0.5659, 0.1616, 0.8084]]
        ]
        expected_output = [
            [1, [[2, math.sqrt(((0.5659-0.2672)**2)+((0.1616-0.5345)**2)+((0.8084-0.8017)**2))]]],
            [2, [[1, math.sqrt(((0.2672-0.5659)**2)+((0.5345-0.1616)**2)+((0.8017-0.8084)**2))]]]
        ]

        self.assertEqual(get_neareast_docs(article_vector_list), expected_output)

    def test_get_nearest_document_3d(self):
        article_vector_list = [
            [1, [1, 2, 3]],
            [4, [10, 9, 8]],
            [2, [5, 1, 4]]
        ]
        expected_output = [
            [1, [[2, math.sqrt(((5-1)**2)+((1-2)**2)+((4-3)**2))],
                [4, math.sqrt(((10-1)**2)+((9-2)**2)+((8-3)**2))]]],
            [4, [[2, math.sqrt(((5-10)**2)+((1-9)**2)+((4-8)**2))],
                [1, math.sqrt(((1-10)**2)+((2-9)**2)+((3-8)**2))]]],
            [2, [[1, math.sqrt(((1-5)**2)+((2-1)**2)+((3-4)**2))],
                [4, math.sqrt(((10-5)**2)+((9-1)**2)+((8-4)**2))]]]
        ]
        self.assertEqual(get_neareast_docs(article_vector_list), expected_output)

if __name__ == '__main__':
    unittest.main()
