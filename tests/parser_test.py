import unittest
import json
from articles import article_class
from articles.json_parser import get_paragraph
from articles.json_parser import remove_duplicates


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
        self.assertEqual(get_paragraph(data), (['sub1 ', 'sub2 '], ['1.1 1.2 ', '2.1 ']))

    def test_get_paragraph_append_all_paragraphs_subheaders_sub2_empty(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"paragraph", "value":"1.1"},
                        {"kind":"paragraph", "value":" 1.2"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub1 ', 'sub2 '], ['1.1  1.2 ', '']))

    def test_get_paragraph_add_all_subheaders(self):
        json_data = """[{"kind":"subheader", "value":"sub1"},
                        {"kind":"subheader", "value":"sub2"}]
                    """
        data = json.loads(json_data)
        self.assertEqual(get_paragraph(data), (['sub1 ', 'sub2 '], ['']))

    def test_is_duplicate(self):
        arts = []
        art = article_class.ArticleClass(
            headline='headline1', publication='nordjyske', author_name='Søren')
        art.data_id = 1
        art.total_words = 5
        arts.append(art)
        arts.append(art)
        result = remove_duplicates(arts)
        self.assertTrue(len(result) == 1)

    def test_is_not_duplicate(self):
        arts = []
        art1 = article_class.ArticleClass(
            headline='headline1', publication='nordjyske', author_name='Søren')
        art2 = article_class.ArticleClass(
            headline='headline1', publication='nordjyske', author_name='Søren')
        art1.data_id = 1
        art2.data_id = 2
        arts.append(art1)
        arts.append(art2)
        result = remove_duplicates(arts)
        self.assertTrue(len(result)==2)
        
    def test_is_not_duplicate_2(self):
        arts = []
        art1 = article_class.ArticleClass(
            headline='headline1', publication='nordjyske', author_name='Søren')
        art2 = article_class.ArticleClass(
            headline='headline1', publication='nordjyske', author_name='Søren')
        art1.total_words = 3
        art1.data_id = 1
        art2.data_id = 1
        art2.total_words = 5
        arts.append(art1)
        arts.append(art2)
        result = remove_duplicates(arts)
        self.assertEqual(result, [art2])



if __name__ == '__main__':
    unittest.main()
