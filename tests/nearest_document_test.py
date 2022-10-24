import unittest
import numpy as np
#from scipy.spatial import distance
from article.find_nearest_document import find_nearest_docs


class TestGetNearestDocs(unittest.TestCase):

    def test_get_nearest_docs(self):
        test_data = [
        {
            1,
            [np.random.rand(1,2000)]
        },
        {
            2,
            [np.random.rand(1,2000)]
        },
        {
            3,
            [np.random.rand(1,2000)]
        },
        {
            4,
            [np.random.rand(1,2000)]
        },
        {
            5,
            [np.random.rand(1,2000)]
        }
        ]
        self.assertEqual(find_nearest_docs(test_data), [1, {}])
        
    if __name__ == '__main__':
    unittest.main()