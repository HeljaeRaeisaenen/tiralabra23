import unittest
from random import randint
import constants
from markov_process import Markov
from trie import Trie, Node
from read_file import split_into_words

class TestMarkovProcess(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/ilike.txt'
        constants.initialize(path)

        self.sentences = constants.SENTENCES
        trie = Trie(Node(), 3)
        sentence = self.sentences[0]
        trie.insert(sentence)

        self.markov = Markov(trie)

    def test_generating_sentence_possible_with_many_starting_words(self):
        w = 'I like'

        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence(w, 3)

        self.assertIn('I', result)
        self.assertIn('like', result)

        test = ('cats' in result) or ('oranges' in result)
        print(result)
        self.assertTrue(test)

    def test_generating_sentence_possible_with_one_starting_word(self):
        w = 'You'

        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence(w, 3)

        test = ('melons' in result) or ('bananas' in result) or ('cats' in result) or ('oranges' in result)
        print(result)
        self.assertTrue(test)

    def test_generating_sentence_possible_with_no_starting_word(self):
        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence('', 3)

        self.assertTrue(result)

    def test_invalid_starting_word_return_false(self):
        result = self.markov.generate_sentence('ooppera', 3)

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
        # but once in a while this test fails randomly. Therefore it's given 3 chances
        comparison_result = []
        for i in range(1,3):
            result = self.markov.generate_sentence('Silloin', degree)
            result2 = self.markov.generate_sentence('Silloin', degree)
            comparison_result.append(result == result2)


        self.assertIn(False, comparison_result)

    def test_result_is_possible_considering_training_material(self):
        self.markov.trie.fill_with_words()

        result = self.markov.generate_sentence('', 2)
        result = split_into_words(result)
        end = 2
        for i in range(len(result)-2):
            found = self.markov.trie.search(result[i:end])
            self.assertTrue(found)
            end += 1
