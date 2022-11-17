import unittest
import json
from articles import article_class
from articles.json_parser import get_paragraph
from articles.json_parser import is_not_duplicate


class TestParserGetParagraph(unittest.TestCase):

    def test_get_paragraph_append_all_paragraphs(self):
        json_data = """[{"kind":"paragraph", "value":"1"},
                        {"kind":"paragraph", "value":" 2 "},
                        {"kind":"paragraph", "value":"3"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), ([], ['1  2  3 ']))

    def test_get_paragraph_one_subheader_append_all_paragraphs(self):
        json_data = """[{"kind":"subheader", "value":"sub"},
                        {"kind":"paragraph", "value":"1"},
                        {"kind":"paragraph", "value":"2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub '], ['1 2 ']))

    def test_get_paragraph_append_all_paragraphs_subheaders(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"paragraph", "value":"1.1"},
                        {"kind":"paragraph", "value":"1.2"},
                        {"kind":"subheader", "value":"sub2"},
                        {"kind":"paragraph", "value":"2.1"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(
            data), (['sub1 ', 'sub2 '], ['1.1 1.2 ', '2.1 ']))

    def test_get_paragraph_append_all_paragraphs_subheaders_sub2_empty(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"paragraph", "value":"1.1"},
                        {"kind":"paragraph", "value":" 1.2"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(
            data), (['sub1 ', 'sub2 '], ['1.1  1.2 ', '']))

    def test_get_paragraph_add_all_subheaders(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub1 ', 'sub2 '], ['']))

    def test_is_duplicate(self):
        art_input = article_class.ArticleClass(
            headline='lol en hund', publication='nordjyske', author_name='Søren')
        art_input.data_id = 1
        art_input.total_words = 5
        self.assertFalse(is_not_duplicate([art_input], art_input))

    def test_is_not_duplicate(self):
        art_input = article_class.ArticleClass(
            headline='lol en hund', publication='nordjyske', author_name='Søren')
        art_input.data_id = 1
        art_input.total_words = 5
        art_copy = art_input
        art_copy.data_id = 2
        art_copy.total_words = 3
        self.assertTrue(is_not_duplicate([art_copy], art_input))


if __name__ == '__main__':
    unittest.main()
