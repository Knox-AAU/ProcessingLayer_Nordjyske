import unittest
import numpy as np
#from scipy.spatial import distance
from article.find_nearest_document import find_nearest_docs


class TestGetNearestDocs(unittest.TestCase):
        
    def test_get_nearest_docs(self):
        input = [[1,[1,2,3,4,5,6,7,8,9,10]],[2,[10,9,8,7,10,9,8,7,6,5]],[3,[11,11,11,11,11,11,11,11,11,11]]]
        expected = [
            [
                1,
                [
                    2,
                    15.297058540778355
                ],
                [
                    3,
                    19.621416870348583
                ]
            ],
            [
                2,
                [
                    1,
                    15.297058540778355
                ],
                [
                    3,
                    11.0
                ]
            ],
            [
                3,
                [
                    1,
                    19.621416870348583
                ],
                [
                    2,
                    11.0
                ]
            ]
        ]
        output = find_nearest_docs(input)
        self.assertListEqual(output, expected)
        #np.testing.assert_array_equal(output, expected)

    if __name__ == '__main__':
        unittest.main()
