import unittest
import constants
from markov_process import Markov
from trie import Trie, Node


class TestRead_file(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/ilike.txt'
        constants.init(path)

        self.sentences = constants.SENTENCES
        trie = Trie(Node())
        sentence = self.sentences[0]
        trie.insert(sentence)

        self.markov = Markov(trie)

    def test_random_sentence(self):
        sentence = self.markov.create_sentence_random('I')

        self.assertEqual('I like cats.', sentence)

    def test_generate_sentence(self):
        w = 'I like'

        self.markov.trie.fill_with_sentences()

        self.markov.generate_sentence(w, 2)
