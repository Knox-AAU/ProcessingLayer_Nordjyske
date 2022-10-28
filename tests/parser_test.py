import unittest
import json
from article.json_parser import is_valid
from article.json_parser import get_paragraph


class TestParserIsValid(unittest.TestCase):

    def test_is_valid_all_empty(self):
        json_data = '{"headline":"", "paragraphs":[], "publication":""}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))

    def test_is_valid_paragraphs_empty(self):
        json_data = '{"headline":"asdads", "paragraphs":[], "publication":"kads"}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))


class TestParserGetParagraph(unittest.TestCase):

    def test_get_paragraph_append_all_paragraphs(self):
        json_data = """[{"kind":"paragraph", "value":"1"},
                        {"kind":"paragraph", "value":" 2 "},
                        {"kind":"paragraph", "value":"3"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), ([], ['1 2 3']))

    def test_get_paragraph_one_subheader_append_all_paragraphs(self):
        json_data = """[{"kind":"subheader", "value":"sub"},
                        {"kind":"paragraph", "value":"1"},
                        {"kind":"paragraph", "value":"2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub'], ['12']))

    def test_get_paragraph_append_all_paragraphs_subheaders(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"paragraph", "value":"1.1"},
                        {"kind":"paragraph", "value":" 1.2"},
                        {"kind":"subheader", "value":"sub2"},
                        {"kind":"paragraph", "value":"2.1"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(
            data), (['sub1', 'sub2'], ['1.1 1.2', '2.1']))

    def test_get_paragraph_append_all_paragraphs_subheaders_sub2_empty(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"paragraph", "value":"1.1"},
                        {"kind":"paragraph", "value":" 1.2"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(
            data), (['sub1', 'sub2'], ['1.1 1.2', '']))

    def test_get_paragraph_add_all_subheaders(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub1', 'sub2'], ['']))


if __name__ == '__main__':
    unittest.main()
