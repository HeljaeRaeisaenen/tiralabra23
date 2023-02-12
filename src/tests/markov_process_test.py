import unittest
from random import randint
import constants
from markov_process import Markov
from trie import Trie, Node


class TestMarkovProcess(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/ilike.txt'
        constants.initialize(path)

        self.sentences = constants.SENTENCES
        trie = Trie(Node(), 2)
        sentence = self.sentences[0]
        trie.insert(sentence)

        self.markov = Markov(trie)

    def test_generating_sentence_possible_with_many_starting_words(self):
        w = 'I like'

        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence(w, 2)

        self.assertIn('I', result)
        self.assertIn('like', result)

        test = ('cats' in result) or ('oranges' in result)
        self.assertTrue(test)

    def test_generating_sentence_possible_with_one_starting_word(self):
        w = 'You'

        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence(w, 2)

        self.assertEqual('You like melons?', result)

    def test_generating_sentence_possible_with_no_starting_word(self):
        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence('', 2)

        self.assertTrue(result)

    def test_invalid_starting_word_return_false(self):
        result = self.markov.generate_sentence('ooppera', 2)

        self.assertFalse(result)

    def test_process_not_deterministic(self):
        # with a reasonable degree
        path = 'tests/testdata/santeri_ivalo_kreivin_aikaan.txt'
        constants.initialize(path)

        degree = randint(1, 5)
        trie = Trie(Node(), degree)
        trie.fill_with_words()
        self.markov = Markov(trie)

        # The chance to generate the same sentence twice should be very low
        # but once in a while this test fails randomly. Run it again and it't ok
        result = self.markov.generate_sentence('Silloin', degree)
        result2 = self.markov.generate_sentence('Silloin', degree)
        print(degree)
        print(result, '\n', result2)

        self.assertNotEqual(result, result2)
