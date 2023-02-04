import unittest
from read_file import read_file


class TestRead_file(unittest.TestCase):
    # def setUp():
    #    pass

    def test_read_file_finds_sentences(self):
        path = 'tests/testdata/catsanddogs.txt'

        sentences = read_file(path)

        self.assertEqual(sentences[0], ['i', 'like', 'cats', '.'])
        self.assertEqual(sentences[-1], ['i', 'often', 'wonder', 'what',
                         'is', 'it', 'like', 'to', 'be', 'a', 'cat', 'or', 'a', 'dog', '.'])

    def test_read_file_can_deal_with_periods_inside_sentences(self):
        path = ''
