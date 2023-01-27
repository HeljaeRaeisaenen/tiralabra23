import unittest
from read_file import read_file


class TestRead_file(unittest.TestCase):
    # def setUp():
    #    pass

    def test_read_file_finds_sentences(self):
        '''catsanddogs.txt has 12 sentences.'''
        path = 'tests/testdata/catsanddogs.txt'

        sentences = read_file(path)

        self.assertEqual(sentences[0], ['I', 'like', 'cats', '.'])
        self.assertEqual(sentences[-1], ['I', 'often', 'wonder', 'what',
                         'is', 'it', 'like', 'to', 'be', 'a', 'cat', 'or', 'a', 'dog', '.'])
