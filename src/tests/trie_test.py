import unittest
from trie import Trie, Node
from read_file import read_file


class TestTrieAndNode(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/catsanddogs.txt'
        self.sentences = read_file(path)
        ALPHABET = set()
        ALPHABET.update(*self.sentences)

        self.trie = Trie(Node())
        sentence = self.sentences[0]
        self.trie.insert(sentence)

    def test_nodes_are_added_with_insert_method(self):
        sentence = self.sentences[0]

        self.assertIsInstance(self.trie.root.children[sentence[0]], Node)

    def test_adding_once_added_sentence_doesnt_do_weird(self):
        sentence = self.sentences[0]
        self.trie.insert(sentence)

        self.assertIsInstance(self.trie.root.children[sentence[0]], Node)

    def test_whole_sentence_is_correctly_inside_trie(self):
        rep = str(self.trie.root)

        self.assertEqual(
            rep, "\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [], value: cats, True)], value: like, False)], value: I, False)], value: None, False)")

    def test_terminal_value_assigned_right(self):
        self.trie.insert(self.sentences[1])

        self.assertEqual(
            self.trie.root.children['I'].children['like'].children['cats'].terminal, True)
        self.assertEqual(
            self.trie.root.children['You'].children['like'].children['dogs'].terminal, True)
