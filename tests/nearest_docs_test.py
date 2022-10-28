import unittest
import numpy as np
from article.find_nearest_document import get_neareast_docs
import math


class TestGetNearestDocument (unittest.TestCase):
    def test_get_nearest_document(self):
        article_vector_list = [
            [1, [1, 2, 3]],
            [2, [10, 9, 8]]
        ]
        expected_output = [
            [1, [2, math.sqrt(((10-1)**2)+((9-2)**2)+((8-3)**2))]],
            [2, [1, math.sqrt(((1-10)**2)+((2-9)**2)+((3-8)**2))]]
        ]
        print(expected_output)
        print(get_neareast_docs(article_vector_list))

        self.assertEqual(get_neareast_docs(
            article_vector_list), expected_output)

    def test_get_nearest_document_stress(self):
        total_docs = 10
        vec_dimensions = 10
        input_list = []
        i = 0
        while i <= total_docs:
            input_list.append([i][np.random.rand(1, vec_dimensions)])
            i = i+1
        self.assertTrue(get_neareast_docs(input_list))


if __name__ == '__main__':
    unittest.main()
