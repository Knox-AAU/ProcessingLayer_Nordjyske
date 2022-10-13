import unittest
import json
from article.json_parser import is_valid

class TestParserIsValid(unittest.TestCase):

    def test_is_valid(self):
        json_data = '{"headline":"", "paragraphs":[], "publication":""}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))

    def test_is_valid(self):
        json_data = '{"headline":"asdads", "paragraphs":[], "publication":"kads"}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))


if __name__ == '__main__':
    unittest.main()
    