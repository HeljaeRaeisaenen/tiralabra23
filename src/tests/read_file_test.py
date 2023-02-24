import unittest
from read_file import read_file
import constants


class TestRead_file(unittest.TestCase):

    def test_read_file_finds_sentences(self):
        path = 'tests/testdata/catsanddogs.txt'

        sentences = read_file(path)

        self.assertEqual(sentences[0], ['I', 'like', 'cats', '.'])
        self.assertEqual(sentences[-1], ['I', 'often', 'wonder', 'what',
                         'is', 'it', 'like', 'to', 'be', 'a', 'cat', 'or', 'a', 'dog', '.'])

    def test_read_file_can_deal_with_periods_inside_sentences(self):
        path = 'tests/testdata/periods.txt'
        sentences = read_file(path)
        self.assertEqual(sentences[0], ['This', 'text', 'contains', 'periods', 'e.g.', 'in',
                                        'names', 'like', 'Dr.', 'A.', 'and', 'Mr.', 'Smith', '.'])

    def test_alphabet_contains_punctuation_chars(self):
        path = 'tests/testdata/santeri_ivalo_kreivin_aikaan.txt'
        constants.initialize(path)

        self.assertIn(',', constants.ALPHABET)
        self.assertIn('.', constants.ALPHABET)
        self.assertIn(':', constants.ALPHABET)

    def test_reading_folders_possible(self):
        path = 'tests/testdata'

        sentences = read_file(path)

        self.assertGreater(len(sentences), 0)