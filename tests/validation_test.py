import unittest
import json
from article.validation import is_valid

class TestValidation(unittest.TestCase):

    def test_is_valid_all_empty(self):
        json_data = '{"headline":"", "paragraphs":[], "publication":""}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))

    def test_is_valid_paragraphs_empty(self):
        json_data = '{"headline":"asdads", "paragraphs":[], "publication":"kads"}'
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))

    def test_is_valid_valid1(self):
        json_data = """{"headline":"text", "paragraphs":[
            {"kind": "paragraph", "value": "test"},
            {"kind": "paragraph", "value": "test2"}],
            "publication":"pub", "byline": {"name": "k", "email": "k@dk.dk"},
            "published_at": "t", "publisher": "Nordjyske Medier","publication": "h"}"""
        data = json.loads(json_data)
        self.assertTrue(is_valid(data))

    def test_is_valid_valid2(self):
        json_data = """{"headline":"text", "paragraphs":[
            {"kind": "subheader", "value": "sub"},
            {"kind": "paragraph", "value": "test"}],
            "publication":"pub", "byline": {"name": "k"},
            "published_at": "t", "publisher": "Nordjyske Medier","publication": "h"}"""
        data = json.loads(json_data)
        self.assertTrue(is_valid(data))

    def test_is_valid_not_nordjyske(self):
        json_data = """{"headline":"text", "paragraphs":[
            {"kind": "subheader", "value": "sub"},
            {"kind": "paragraph", "value": "test"}],
            "publication":"pub", "byline": {"name": "te"},
            "published_at": "te", "publisher": "Nordjyske Medie","publication": "te"}"""
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))

    def test_is_valid_not_enough_paragraphs(self):
        json_data = """{"headline":"text", "paragraphs":[
            {"kind": "paragraph", "value": "test"}],
            "publication":"pub", "byline": {"name": "k", "email": "k@dk.dk"},
            "published_at": "t", "publisher": "Nordjyske Medier","publication": "h"}"""
        data = json.loads(json_data)
        self.assertFalse(is_valid(data))
    