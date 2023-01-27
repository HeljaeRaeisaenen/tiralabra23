import unittest
from trie import Trie, Node
import constants


class TestTrieAndNode(unittest.TestCase):
    def setUp(self):
        path = 'tests/testdata/catsanddogs.txt'
        constants.init(path)

        self.sentences = constants.SENTENCES
        self.trie = Trie(Node())
        sentence = self.sentences[0]
        self.trie.insert(sentence)

    def test_node(self):
        node = Node()
        x = node.give_children()

        self.assertEqual(x, [])

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
            rep, "\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [\n<class 'trie.Node'>(children: [], value: ., freq.: 1)], value: cats, freq.: 1)], value: like, freq.: 1)], value: I, freq.: 1)], value: None, freq.: 0)")

    def test_terminal_value_assigned_right(self):
        self.trie.insert(self.sentences[1])

        self.assertEqual(
            self.trie.root.children['I'].children['like'].children['cats'].children['.'].terminal, True)
        self.assertEqual(
            self.trie.root.children['You'].children['like'].children['dogs'].children['.'].terminal, True)

    def test_search_quick_trie(self):
        self.trie.fill_with_sentences()

        children = self.trie.search_quick('cat')

        self.assertEqual(len(children), 6)
