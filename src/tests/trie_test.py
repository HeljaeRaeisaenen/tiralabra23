import unittest
from trie import Trie, Node
import constants


class TestTrieAndNode(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/catsanddogs.txt'
        constants.initialize(path)

        self.sentences = constants.SENTENCES
        self.trie = Trie(Node(), 2)
        sentence = self.sentences[0]
        self.trie.insert(sentence)

    def test_node_exists(self):
        node = Node()
        x = node.give_children()

        self.assertEqual(x, [])

    def test_nodes_are_added_with_insert_method(self):
        sentence = self.sentences[0]

        self.assertIsInstance(self.trie.root.children[sentence[0]], Node)

    def test_whole_sentence_is_correctly_inside_trie(self):
        sentence = self.sentences[0]

        node = self.trie.root
        for word in sentence:
            node = node.children[word]            
            self.assertEqual(word, node.value)

    #def test_terminal_value_assigned_right(self):
    #    self.trie.insert(self.sentences[1])
    #
    #    self.assertEqual(
    #        self.trie.root.children['i'].children['like'].children['cats'].children['.'].terminal, True)
    #    self.assertEqual(
    #        self.trie.root.children['you'].children['like'].children['dogs'].children['.'].terminal, True)

    def test_search_trie(self):
        self.trie.fill_with_words()
        s = ['i', ' ', 'like', ' ']
        result = self.trie.search(s)
        self.assertEqual(result[0].value, 'cats')
